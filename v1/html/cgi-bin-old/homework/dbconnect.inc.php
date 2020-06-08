<?php
  $sqlname = 'homer';
  $sqlpassword = '6194634453';

  function selectDB($dbname, $dbcnx) {
    if (!@mysql_select_db($dbname, $dbcnx)) {
      exit('Error opening the database');
    return (false);
    } else {
    return (true);
    } 
  }
  
  function connectDB($sqlname, $sqlpassword) {
    $dbcnx = @mysql_pconnect('localhost', $sqlname, $sqlpassword);
    if (!$dbcnx) {
      exit('The Patrick Henry Patriot Exhibition website is down for maintenance.  Check back again later.');
    }
  return ($dbcnx);
  }

  $dbcnx = connectDB($sqlname, $sqlpassword);
  selectDB('chemistry', $dbcnx);
  $config = @mysql_fetch_array(@mysql_query("SELECT * FROM config LIMIT 1"));
?>
