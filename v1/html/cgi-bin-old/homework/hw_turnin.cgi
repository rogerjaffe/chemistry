#!c:\perl\bin\perl.exe

# Author: Nathan Wiger
# Last Modified: 06/28/98
#
# This single file handles all user interaction across the CGI. It posts
# the initial values given to it and makes an HTML document, and then
# takes the input back in again and sends it to the actual processor.
# Pretty slick...

# You need to set these variables correctly...

# Where email goes:
$webmaster="rjaffe\@sandi.net";

# The actual, last step homework processor (i.e., the one that writes the data)
#$hw_processor="http://chemistry2.csudh.edu/cgi-bin/SOMETHING.pl";

# The list of valid instructors, in Perl array form (you can continue it on 
# multiple lines if you need to):
@instructors = ("Voss");


require "cgistrings.pl";             #for converting cgi strings
# print "Content-type: text/html\n\n";

&parse_form_data(*simple_form);
&create_output(*simple_form);
exit(0);

sub parse_form_data {

   local(*FORM_DATA) = @_;

   local($request_method, $query_string, @key_value_pairs, @key_value, $key, $value);

   $request_method = $ENV{'REQUEST_METHOD'};

   if($request_method eq "GET") {
      $query_string = $ENV{'QUERY_STRING'};
   } elsif($request_method eq "POST") {
      read(STDIN, $query_string, $ENV{'CONTENT_LENGTH'});
   } else {
      &return_error(500, "Server Error", "This request uses an unsupported method");
   }

   @key_value_pairs = split(/&/, $query_string);

   foreach $key_value (@key_value_pairs) {
      ($key, $value) = split(/=/, $key_value);

      $tmp = $value;
      $value = &cgi_to_normal($tmp); #from cgistrings.pl

      if(defined($FORM_DATA{$key})) {
         $FORM_DATA{$key} = join(" ", $FORM_DATA{$key}, $value); 
      } else {
         $FORM_DATA{$key} = $value;
      }

   }
}

sub create_output {
   
   local(*FORM_DATA) = (@_);

   print <<End_of_Header;

<html>
<title>Chemistry Homework Submission</title>
<body bgcolor=white text=black link=blue alink=blue vlink=0000BB>
<font face=arial,helvetica>
<!-- NOTE: This form is generated by the hw_turnin.cgi Perl script -->
<h3>Enter Your name and Select Your Instructor</h3>
To finish submitting your homework, please enter your name and then choose the 
appropriate instructor from the list below:<br>
<br></font>
<form method="POST" action="homework_processor.php">
Your Name: <input type=text name="yourname" size=30><br>
Your Instructor: <select name="instructor">
End_of_Header

   foreach $instructor (@instructors) {
      print "<option value=\"$instructor\">$instructor\n";
   }

   print "</select><br>\n";

   while(($key, $value) = each(%FORM_DATA)) {
     print "<input type=hidden name=\"$key\" value=\"$value\">\n";
   }
    
print <<End_of_Footer;
<br>
<center><br>
<input type=submit value=" Submit! "> <input type=reset value=" Reset ">
</form>
</html>

End_of_Footer

}

sub return_error {

   local($status, $keyword, $message) = @_;

  print <<End_of_Error;

   <html>
   <title>Unexpected CGI Error</title>
   <body bgcolor=white text=black>
   <font face=arial,helvetica>
   <h1>$status $keyword</h1>
   <h3>$message</h3>
   Please contact <a href="mailto:$webmaster"><i>$webmaster</i></a> for
   more information.
   </html> 

End_of_Error

   exit(1);
}


