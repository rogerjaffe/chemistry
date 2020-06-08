#homework.setup.cgi
#
#######################################################################
#                         Email Variables                             #
#######################################################################
$email_to = "kvoss\@sandi.net";
#######################################################################
#                       Location Variables                            #
#######################################################################   

$location_of_mail_lib = "mail-lib.pl";
$location_of_setup_file = "homework.setup.cgi";

#######################################################################
#                  Database Variables                                 #
#######################################################################
$get_dbase_from_form = "yes";
$should_I_append_a_database = "yes";
$dbase = "/home/httpd/cgi-bin/Form_processor/Databases/feedback.data";
$database_delimiter = ",";

#######################################################################
#                  Defining your Fields                               #
#######################################################################

@form_variables = ("yourname",
		   "instructor",
		   "page",
		   "total",
		   "correct",
		   "verify",
		   "time"); 

%form_variable_name_map = ("yourname",		"Name",
			   "instructor",	"Instructor",
			   "page",		"Page",
			   "total",		"Total",
			   "correct",		"Correct",
			   "verify",		"Verif.No",
			   "time",		"Time");

@required_variables = ("yourname", "instructor");

#######################################################################
#                    Miscellaneous Options                            #
#######################################################################

$current_century = "20";
$should_user_verify = "no";

#######################################################################
#                 required_fields_error_message Subroutine            #
#######################################################################
                           
sub required_fields_error_message
  {
  print "Content-type: text/html\n\n"; 
  print qq~
  <HTML>
  <HEAD>
  <TITLE>Error in Processing Form - Required Fields</TITLE>
  </HEAD>
  <BODY BGCOLOR = "FFFFFF" TEXT = "000000">

  <BLOCKQUOTE>

  <H2>
  Woops, I'm sorry, the following fields are required:

  <UL>
  <LI>Name
  <LI>Instructor
  </UL>

  Please click the "back" button on your browser or click <A HREF =
  "$url_of_the_form">here</A> to go back and make sure you fill out all
  the required information.
  </H2>

  </BLOCKQUOTE>
  </BODY>
  </HTML>~;
  }

#######################################################################
#                 cannot_find_database Subroutine                     #
#######################################################################
  
sub cannot_find_database
  {
  print "Content-type: text/html\n\n";
  print qq~
  <HTML>
  <HEAD>
  <TITLE>Form Processing Error - Database Access</TITLE>
  </HEAD>
  <BODY BGCOLOR = "FFFFFF" TEXT = "000000">
 
  <H2>
  <BLOCKQUOTE>
  I'm sorry, I am having trouble finding the database that this

  information should be sent to.  Please contact 
  <A HREF = "mailto:$email_to">$email_to</A> and let us know that there
  has been a problem.  Thank you very much and sorry about the
  inconvenience.
  </BLOCKQUOTE>
  </H2>
  </BODY>
  </HTML>~;
  }

#######################################################################
#                        HTML Reply Subroutines                       #
#######################################################################
                
sub html_reply_header
  {
  print "Content-type: text/html\n\n";
  print qq~
  <HTML>
  <HEAD>
  <TITLE>Thank you</TITLE>
  </HEAD>
  <BODY BGCOLOR = "FFFFFF" TEXT = "000000">
  <H4>~;
  }

sub html_reply_body
  {
  print qq~
Thank you. Your data has been successfully submitted.<br>You should print this page for your records. 
</h4><blockquote><TABLE>~;

  foreach $variable (@form_variables)
    {
    print qq~
    <TR VALIGN = "top">
    <TH ALIGN = "left" VALIGN = "top">$form_variable_name_map{$variable}</TH>
    <TD>$form_data{$variable}</TD>
    </TR>~;
    }
  print qq~
  </TABLE>
</BLOCKQUOTE>~;
  }

sub html_reply_footer
  {
  print qq~
  <br><a href="../../homework/hwintro.html">Back to Homework Pages</a>
  </BODY>
  </HTML>~;
  }

1;
