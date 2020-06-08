<?php session_start(); ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><!-- InstanceBegin template="/Templates/Default.dwt.php" codeOutsideHTMLIsLocked="false" -->
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<!-- InstanceBeginEditable name="doctitle" -->
<title>PHHS Chemistry Practice</title>
<!-- InstanceEndEditable --><!-- InstanceBeginEditable name="head" --><!-- InstanceEndEditable -->
<link href="chemistry.css" rel="stylesheet" type="text/css" />
<style>
@media print { DIV.PAGEBREAK {page-break-after: always}}
</style>
<!-- InstanceBeginEditable name="onLoad" -->
<script language="JavaScript" type="text/javascript" src="cal2.js"></script>
<script language="JavaScript" type="text/javascript" src="cal_conf2.js"></script>
<!-- InstanceEndEditable -->
</head>

<body>

<strong>Patrick Henry Chemistry Practice</strong><br />
<!-- InstanceBeginEditable name="PageTitle" -->View Student Results<!-- InstanceEndEditable --><br />
<?php
// Begin authorization test
  include '../../../../includes/userSession.php';
  include_once 'dbconnect.inc.php'; 
  $userSession = new userSession($dbcnx);
  $userSession->validateSession($_SESSION['sessionID'], $sessionVariables);
  if ($sessionVariables['Chemistry']['Authenticate']) {
?>

<a href="index.php">Home</a><br />
<!-- InstanceBeginEditable name="Content" -->
<br />
<b>The homework practice website is at</b> <a href="http://henry.sandi.net/chemistry/homework/hwintro.html">http://henry.sandi.net/chemistry/homework/hwintro.html</a>
<?php
  include '../../../../maintenance/functions/date_utilities.inc.php';
  $fromDate = $_POST['fromdate'];
  $toDate = $_POST['todate'];
  if (!$fromDate) {                    
    $fromDate = date('m/d/Y', mktime(0,0,0,date('m'), date('d')-7, date('Y')));
    $toDate = date('m/d/Y', mktime(23,59,59,date('m'), date('d'), date('Y')));
  }
    
?>
<form name="form1" id="form1" action="index.php" method="post">
<p><b>Show students submitting chemistry work between</b>&nbsp; 
<input name="fromdate" type="text" id="fromdate" size="10" maxlength="10" value="<?php echo $fromDate; ?>" />
  (<a href="javascript:showCal('fromdate')">Select date</a>)&nbsp;and&nbsp;
<input name="todate" type="text" id="todate" size="10" maxlength="10" value="<?php echo $toDate; ?>" />
  (<a href="javascript:showCal('todate')">Select date</a>)
&nbsp;<input name="submit" type="submit" id="submit" value="Submit" />
  
</form>

<?php
  function format_td($text) {
    return ("<td>$text</td>");
  }
  if ($_POST['submit']) {
    $zangleID = $sessionVariables['zangleID'];
    $fromDateSQL = date_DisplayToSQL($fromDate) . " 00:00:00";
    $toDateSQL = date_DisplayToSQL($toDate) . " 23:59:59";
    $sql = "SELECT records.*, lop.lop_students.LastName, lop.lop_students.FirstName
      FROM records 
      JOIN lop.lop_students ON
        lop.lop_students.StuID=records.StuID
      WHERE (\"$fromDateSQL\"<=Date) AND (Date<=\"$toDateSQL\")";
	if (!$sessionVariables['Chemistry']['Administrator']) {
      $sql .= " AND TeacherID=\"$zangleID\"";
	}
	$sql .= " ORDER BY LastName, FirstName";
    $students = @mysql_query($sql);
    echo "<table border=\"0\" width=\"100%\">
      <tr><td width=\"15%\"><b>Student name</b></td>
      <td width=\"20%\"><b>Page</b></td>
      <td width=\"5%\"><b>Correct</b></td>
      <td width=\"5%\"><b>Total</b></td>
      <td width=\"10%\"><b>Verify</b></td>
      <td width=\"15%\"><b>Date</b></td></tr>";
      
    while ($student = @mysql_fetch_array($students)) {
      echo "<tr>";
      echo format_td($student['LastName'] . ", " . $student['FirstName']);
      echo format_td($student['Page']);
      echo format_td($student['Correct']);
      echo format_td($student['Total']);
      echo format_td($student['Verify']);
      echo format_td($student['Date']);      
      echo "</tr>";
    }
    echo "</table>";
  }  
?>

<!-- InstanceEndEditable -->
<?php
  } else {
    echo "<p><font color=\"#FF0000\"><b>You are not authorized for this system</b></font></p>";
  }
?>
<p class="small_font">Patriot Internet Information System <br />
Copyright 2008 Roger Jaffe<br />
Version <?php echo $config['Version']; ?></p>
</body>
<!-- InstanceEnd --></html>
