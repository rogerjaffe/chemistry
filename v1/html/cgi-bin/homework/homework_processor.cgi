#!c:\perl\bin\perl.exe 

# Name: homework_processor.cgi
#
# Last Modified: 6-9-98
#
# Copyright: The core of this application is Form_processor 5.0,written by 
# Selena Sol(selena@eff.org, http://www.extropia.com) and Gunther Birznieks
# (birzniek@hlsun.redcross.org) who generously have made it available to 
# the Web community.  It has been modified by George Wiger 
# gwiger@chemistry.csudh.edu) to fulfil the special nature of this project.
# In particular, a number of routines have been removed from the source file
# and the handling of database files has been modified. Feel free to copy,
# cite, reference, sample, borrow, or plagiarize the contents. Users
# are strongly encouraged to look at the Form_processor 5.0 to get a full
# sense of the capabilities of the script. Information wants
# to be free, support public domain freeware. 
#######################################################################
#                  Flush the Perl Buffer. 		   	      #
#######################################################################

		# The script begins by telling the Perl interpreter that
		# it should continuously flush its buffer so that text
		# from this script is sent directly to the Web Browser.
		# We do this to streamline debugging and make sure that
		# the script operates with the flow we want it to.

$| = 1;

#######################################################################
#               Read and Parse Form Data                  	      #
#######################################################################

		# Next, the ReadParse subroutine in cgi-lib.pl is used to
		# read the incoming form data. However, the subroutine is
		# sent "form_data" as a parameter so that the associative
		# array of form keys/values comes back with a descriptinve
		# name rather than just %in. 

&require_supporting_libraries (__FILE__, __LINE__,
                              "cgi-lib.pl");  
&ReadParse(*form_data);

#######################################################################
#                        Load Supporting Files                        #
#######################################################################

		# Once it has read the incoming form data, the script
		# will be able to determine which setup file it should
		# use to process the incoming form data.  
		#
		# Perhaps a bit of explanation is in order.
		#
		# Every HTML form which utilizes this application as a
		# backend MUST include a "hidden" form variable called
		# "setup_file" using the following syntax somewhere
		# between the <FORM> and </FORM> tags:
		#
		# <INPUT TYPE = "hidden" NAME = "setup_file" 
		# 	 VALUE = "[NAME OF SETUP FILE]">
		#
		# For example, the following code would define a setup
		# file called download.setup:
		#
		# <INPUT TYPE = "hidden" NAME = "setup_file" 
		#	 VALUE = "download.setup">
		#
		# This variable will provide the name of the file which
		# this script will use to define all of the customizable
		# aspects of its operation.  For example, the setup file
		# defines who the script should E-mail form responses to
		# and what the script should send to the Web Browser as a
		# response when a user submits some information.
		# 
		# The reason for this is that this one script can handle
		# an infinite amount of unique forms.
		#
		# Each form has a corresponding setup file which defines
		# how the script performs.  The logic (and programming)
		# remains the same for all forms.  All that changes are
		# the variables and subroutines in the setup files.  This
		# makes it very easy for you to quickly generate diverse
		# forms with the one backend.
		#
		# So the script first takes the value of "setup_file"
		# coming in from the form (which cgi-lib.pl has already
		# parsed into the %form_data associative array) and
		# assigns it to the variable $setup_file.
		#
		# Then it uses the subroutine
		# require_supporting_libraries documented later in this
		# script to actually load the setup file and all of itsd
		# configuration options.
		#
		# Once the setup file has been loaded, the script also
		# uses the require_supporting_libraries subroutine to
		# load the mail library which we will use to send email to
		# the form administrator.


$setup_file = "homework.setup.cgi";
$setup_file =~ /([\w-.]+setup[\w-.]+)/;
$untainted_setup_file = $1;
&require_supporting_libraries (__FILE__, __LINE__,
                               "$untainted_setup_file");

 print "line 107";
#######################################################################
#                       Check Required Fields                         #
#######################################################################

		# Now that the script has loaded all of the supporting
		# libraries it is time to start processing the incoming
		# form data.  
		#
		# The first thing that the script does is to make sure
		# that the user has filled in data for every field
		# that the administrator has defined as "required".  The
		# list of required fields are defined in the setup file
		# array @required_variables for each separate form to be
		# processed.  
		#
		# The script simply goes through each of the fields and
		# checks to see if it has a value coming in as form data
		# (as stored in the form_data associative aray by
		# cgi-lib.pl).  If the field was left blank, the script
		# accesses the subroutine required_fields_error_message in
		# the setup file which sends the user a note regarding the
		# error and then exits.

foreach $variable (@required_variables)
  {
  if ($form_data{$variable} eq "")
    {
    &required_fields_error_message;
    exit;
    } 
  } 

#######################################################################
#                       Append a Database                             #
#######################################################################

		# Next, the script determines if it has been instructed	
		# in the setup file to append the user-submitteed data to
		# a database file. 
		#
		# If the $should_I_append_a_database variable has been set
		# to yes, the script appends to the database specified by
		# $location_of_database using the database delimiter 
		# $database_delimiter which are both defined in the setup
		# file.

if ($should_I_append_a_database eq "yes")
  {
	#You then check to see whether the database name is in the form
	#or in the setup file. If $get_dbase_from_form is set to yes, the
	#database name is read from the form as $form_data{'database_name'}. 
	#Otherwise, it's read from the setup file as $dbase
	if ($get_dbase_from_form eq "yes")
		{
			$location_of_database="../../savedata/".$form_data{'instructor'}."/homework.txt"
		}
	else
		{
			$location_of_database=$dbase;
		}
		# Before appending to the database, the script checks to
		# make sure that the database file is actually writable by
		# it.
		#
		# If the file is indeed writable, the script creates a new
		# database row made up of field values delimited by the
		# delimter specified in the setup file.
		# This script produces a row with the following format:
		#
		# Student Name,Instructor,Page Title,Total,Correct,verif no,time
		#
		# Notice that because of the quirks of the foreach loop, 
		# we will end each database row with a final database
		# delimiter.  Because we do not want this final delimiter, 
		# the script utilizes the chop operator to remove it.
		#
		# Finally, notice that we will modify client submitted
		# data if it includes the newline character.  Since we are
		# using the newline character to delineate database rows,
		# we do not want the customer to have the ability to embed
		# those characters in their data,.  Thus, we will use
		# the regular expression operator to change all occurances
		# of newlines (\n) with the tag "~nl~".  When we manage
		# the database later, we need only do a find and
		# replace on ~nl~.

if (-w $location_of_database)
    {
    foreach $variable (@form_variables)
      {
      $form_data{$variable} =~ s/\n/~nl~/g; 
      $database_row .= "$form_data{$variable}$database_delimiter";
      } # End of foreach $variable (@form_variables)
    chop $database_row;
	$database_row.="," . &get_date<br />;

		# Next, the script appends the newly created database to
		# the existing database. However, before actually
		# modifying the database file, the script makes sure to
		# use the lockfile routines discussed later in this script
		# to assure that only one instance of the script can
		# modify the file at one time.  Afterall, it would not do
		# for two instances of the script to modify the file at
		# one time.  At best, one of the forms would not be
		# processed correctly.  At worst, the data file might
		# become corrupt.  The lockfile routines prevent more than
		# one instance of the script from accessing the file at
		# one time.

    &get_file_lock ("$location_of_database.lock");

		# Once the lock file has been created, the script opens up
		# the datafile for appending using the (>>) operator.
		# However, if it has a problem opening the database file,
		# it sends a useful debugging message to the Web Browser
		# using the subroutine &file_open_error discussed later in
		# this script.
		#
		# Once the database is opened, the script appends the new
		# database row to the end of the file and closes the file
		# again, removing the lockfile as well.

    open (DATABASE, ">>$location_of_database") || 
         &file_open_error("$location_of_database", "Append a Database",
			  _FILE__, __LINE__);     

    print DATABASE "$database_row\n";
    close (DATABASE);
    &release_file_lock ("$location_of_database.lock");
    } # End of if (-w $location_of_database)

		# If the database file was not writable, the script
		# sends an error message back to the user.  

  else
    {
    &cannot_find_database;
    exit;
    }
  } # End of if ($should_I_append_a_database eq "yes")

#######################################################################
#                       Respond to the Client                         #
#######################################################################

		# The script sends an HTML response to the client.
		# using several subroutines defined in the setup
		# file so that you can easily customize this HTML code.
  $current_date = &get_date;
  &html_reply_header;
  &html_reply_body;
  print qq~
  $current_date~;
  &html_reply_footer;
#################################################################
#                      get_date Subroutine                      #
#################################################################

                # get_date is used to get the current date and time and
                # format it into a readable form.  The subroutine takes no
                # arguments and is called with the following syntax:      
                #
                # $date = &get_date;
                #
                # It will return the value of the current date, so you
                # must assign it to a variable in the calling routine if
                # you are going to use the value.

sub get_date
  {

                # The subroutine begins by defining some local working
                # variables

  local ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst,$date);
  local (@days, @months);

  @days = ('Sunday','Monday','Tuesday','Wednesday','Thursday',      
           'Friday','Saturday');
  @months = ('January','February','March','April','May','June','July',
             'August','September','October','November','December');

                # Next, it uses the localtime command to get the current
                # time, from the value returned by the time
                # command, splitting it into variables.

  ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);

                # Then the script formats the variables and assign them to
                # the final $date variable.  Note that $current_century
                # is defined in web_store.setup.  Since the 20th centruy
                # is really 1901-2000, we'll need to subtract 1 from this
                # value in order to format the year correctly.

  if ($hour < 10)                   
    {
    $hour = "0$hour";
    }
  if ($min < 10)
    {
    $min = "0$min";
    }
  if ($sec < 10)
    { $sec = "0$sec";
    }
  $year = $year + 1900;
#  $date = "$days[$wday],$months[$mon] $mday, $year at $hour\:$min\:$sec";  Original format
  $date = "$mon\/$mday\/$year,$hour\:$min\:$sec";
  return $date;
  }          

#######################################################################
#                       Require Supporting Libraries.                 #
#######################################################################

                # require_supporting_libraries is used to read in some of
                # the supporting files that this script will take
                # advantage of.
                #
                # require_supporting_libraries takes a list of arguments
                # beginning with the current filename, the current line
                # number and continuing with the list of files which must
                # be required using the following syntax:
                #
                # &require_supporting_libraries (__FILE__, __LINE__,
                #                               "file1", "file2",
                #                               "file3"...);      
                #
                # Note: __FILE__ and __LINE__ are special Perl variables
                # which contain the current filename and line number
                # respectively.  We'll continually use these two variables
                # throughout the rest of this script in order to generate
                # useful error messages.     

sub require_supporting_libraries
  {

                # The incoming file and line arguments are split into
                # the local variables $file and $line while the file list
                # is assigned to the local list array @require_files.
                #
                # $require_file which will just be a temporary holder
                # variable for our foreach processing is also defined as a
                # local variable.       

  local ($file, $line, @require_files) = @_;
  local ($require_file);

                # Next, the script checks to see if every file in the
                # @require_files list array exists (-e) and is readable by
                # it (-r). If so, the script goes ahead and requires it.

  foreach $require_file (@require_files)
    {
    if (-e "$require_file" && -r "$require_file" && $require_file ne "./Setup_files/")
      {
      require "$require_file";
      }

                # If not, the scripts sends back an error message that
                # will help the admin isolate the problem with the script.   

    else
      {
#      print "Content-type: text/html\n\n";
      print "I am sorry but I was unable to require $require_file at line
            $line in $file.  Would you please make sure that you have the
            path correct and that the permissions are set so that I have
            read access?  Thank you.";
      exit;
      }
    } # End of foreach $require_file (@require_files)
  } # End of sub require_supporting_libraries       

#######################################################################
#                            get_file_lock                            #
#######################################################################

                # get_file_lock is a subroutine used to create a lockfile.
                # Lockfiles are used to make sure that no more than one
                # instance of the script can modify a file at one time.  A
                # lock file is vital to the integrity of your data.
                # Imagine what would happen if two or three people
                # were using the same script to modify a shared file (like
                # the error log) and each accessed the file at the same
                # time.  At best, the data entered by some of the users
                # would be lost.  Worse, the conflicting demands could
                # possibly result in the corruption of the file.
                #
                # Thus, it is crucial to provide a way to monitor and
                # control access to the file.  This is the goal of the
                # lock file routines.  When an instance of this script
                # tries to  access a shared file, it must first check for
                # the existence of a lock file by using the file lock
                # checks in get_file_lock.
                #
                # If get_file_lock determines that there is an existing
                # lock file, it instructs the instance that called it to
                # wait until the lock file disappears.  The script then
                # waits and checks back after some time interval.  If the
                # lock file still remains, it continues to wait until some
                # point at which the admin has given it permissios to just
                # overwrite the file because some other error must have
                # occurred.
                #
                # If, on the other hand, the lock file has dissappeared,
                # the script asks get_file_lock to create a new lock file
                # and then goes ahead and edits the file.
                #
                # The subroutine takes one argumnet, the name to use for
                # the lock file and is called with the following syntax:
                #
                # &get_file_lock("file.name");    

sub get_file_lock
  {
  local ($lock_file) = @_;
  local ($endtime);
  $endtime = 20;
  $endtime = time + $endtime;

                # We set endtime to wait 20 seconds.  If the lockfile has
                # not been removed by then, there must be some other
                # problem with the file system.  Perhaps an instance of
                # the script crashed and never could delete the lock file.

  while (-e $lock_file && time < $endtime)
    {
    sleep(1);
    }           

  open(LOCK_FILE, ">$lock_file") || &file_open_error ("$lock_file", 
						      "Lock File Routine",
						      __FILE__, __LINE__);

                # Note: If flock is available on your system, feel free to
                # use it.  flock is an even safer method of locking your
                # file because it locks it at the system level.  The above
                # routine is "pretty good" and it will server for most
                # systems.  But if youare lucky enough to have a server
                # with flock routines built in, go ahead and uncomment
                # the next line and comment the one above.

# flock(LOCK_FILE, 2); # 2 exclusively locks the file

  }

#######################################################################
#                            release_file_lock                        #     
#######################################################################

                # release_file_lock is the partner of get_file_lock.  When
                # an instance of this script is done using the file it
                # needs to manipulate, it calls release_file_lock to
                # delete the lock file that it put in place so that other
                # instances of the script can get to the shared file.  It
                # takes one argument, the name of the lock file, and is
                # called with the following syntax:
                #
                # &release_file_lock("file.name");

sub release_file_lock
  {
  local ($lock_file) = @_;

# flock(LOCK_FILE, 8); # 8 unlocks the file

                # As we mentioned in the discussion of get_file_lock,
                # flock is a superior file locking system.  If your system
                # has it, go ahead and use it instead of the hand rolled
                # version here.  Uncomment the above line and comment the
                # two that follow.

  close(LOCK_FILE);
  unlink($lock_file);
  }                                                                                              
         

#######################################################################
#                    file_open_error Subroutine                       #
#######################################################################

                # If there is a problem opening a file or a directory, it
                # is useful for the script to output some information
                # pertaining to what problem has occurred.  This
                # subroutine is used to generate those error messages.
                #
                # file_open_error takes four arguments: the file or
                # directory which failed, the section in the code in which 
                # the call was made, the current file name and
                # line number, and is called with the following syntax:
                #
                # &file_open_error("file.name", "ROUTINE", __FILE__,
                #                  __LINE__);

sub file_open_error
  {

                # The subroutine simply uses the update_error_log
                # subroutine discussed later to modify the error log and
                # then uses CgiDie in cgi-lib.pl to gracefully exit the
                # application with a useful debugging error message sent
                # to the browser window.

  local ($bad_file, $script_section, $this_file, $line_number) = @_;
#  print "Content-type: text/html\n\n";
  &CgiDie ("I am, but I was not able to access $bad_file in the
        $script_section routine of $this_file at line number $line_number.
        Would you please make sure the path is correctly defined in
        web_store.setup and that the permissions are correct.")
  }     

#######################################################################
#                    format_text_field Subroutine                     #
#######################################################################

sub format_text_field 
  {
  local($value) = @_;
                # 
                # Very simple. We return the value in
                # $value plus a string of 25 spaces which
                # has been truncated by the length of 
                # the $value string.
                # 
                # This results in a left justified
                # field of width = 25.
                # 
  return($value . substr((" " x 25), length($value)));  

  } # End of format_text_field 
