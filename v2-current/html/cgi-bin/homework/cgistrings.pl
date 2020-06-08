#!c:\perl\bin\perl.exe

# Author: Nathan Wiger <nwiger@ucsd.edu>
# Last Modified: 05/22/98
#
# This is a very simple, useful Perl module for turning things in and out
# of cgi strings. Simply 'require' it in your program, then call it like so:
#
# $new_cgi_string = &normal_to_cgi($normal_string);
# $new_normal_string = &cgi_to_normal($cgi_string);

sub normal_to_cgi {

   local($string) = (@_);

   $string =~ s/\%/\%25/g;
   $string =~ s/\+/\%2B/g;
   $string =~ s/ /\+/g;
   $string =~ s/\//\%2F/g;
   $string =~ s/\n/\%0D\%0A/g;
   $string =~ s/\!/\%21/g;
   $string =~ s/\,/\%2C/g;
   $string =~ s/\$/\%24/g;
   $string =~ s/\#/\%23/g;
   $string =~ s/\&/\%26/g;
   $string =~ s/\^/\%5E/g;
   $string =~ s/\</\%3C/g;
   $string =~ s/\>/\%3E/g;
   $string =~ s/\?/\%3F/g;
   $string =~ s/\|/\%7C/g;
   $string =~ s/\~/\%7E/g;
   $string =~ s/\[/\%5B/g;
   $string =~ s/\]/\%5D/g;
   $string =~ s/\{/\%7B/g;
   $string =~ s/\}/\%7D/g;
   $string =~ s/\"/\%22/g;
   $string =~ s/\'/\%27/g;
   $string =~ s/\:/\%3A/g;
   $string =~ s/\(/\%28/g;
   $string =~ s/\)/\%29/g;
   $string =~ s/\;/\%3B/g;
   $string =~ s/\%3D/\=/g;

   return $string;

}

sub cgi_to_normal {

   local($string) = (@_);

   $string =~ s/\+/ /g;
   $string =~ s/\%2B/\+/g;
   $string =~ s/\%2F/\//g;
   $string =~ s/\%0D\%0A/\n/g;
   $string =~ s/\%21/\!/g;
   $string =~ s/\%2C/\,/g;
   $string =~ s/\%24/\$/g;
   $string =~ s/\%23/\#/g;
   $string =~ s/\%26/\&/g;
   $string =~ s/\%5E/\^/g;
   $string =~ s/\%3C/\</g;
   $string =~ s/\%3E/\>/g;
   $string =~ s/\%3F/\?/g;
   $string =~ s/\%7C/\|/g;
   $string =~ s/\%7E/\~/g;
   $string =~ s/\%5B/\[/g;
   $string =~ s/\%5D/\]/g;
   $string =~ s/\%7B/\{/g;
   $string =~ s/\%7D/\}/g;
   $string =~ s/\%22/\"/g;
   $string =~ s/\%27/\'/g;
   $string =~ s/\%3A/\:/g;
   $string =~ s/\%28/\(/g;
   $string =~ s/\%29/\)/g;
   $string =~ s/\%3B/\;/g;
   $string =~ s/\%3D/\=/g;
   $string =~ s/\%25/\%/g;

   return $string;

}

return 1;