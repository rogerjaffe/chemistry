<?php
include 'dbconnect.inc.php';
$instructorCode = $_POST['instructor'];
$index = substr($instructorCode, 1, 20);
$zangleID = $_POST['h'.$index];
$stuid = $_POST['stuid'.$index];
$correct = $_POST['correct'];
$page = $_POST['page'];
$verify = $_POST['verify'];
$total = $_POST['total'];
$results = $_POST['results'];
$date = date('Y/m/d H:i:s');

$sql = "INSERT INTO records (StuID, TeacherID, Page, Total, Correct, Verify, Date)
  VALUES (\"$stuid\", \"$zangleID\", \"$page\", $total, $correct, \"$verify\", \"$date\")";
@mysql_query($sql);

$sql = "SELECT * FROM teachers WHERE ZangleID=\"$zangleID\"";
$teacher = @mysql_fetch_array(@mysql_query($sql));
$teacherName = $teacher['Name'];
  
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>PHHS Chemistry Practice System</title>
</head>
<body>
<p><b>Great job working on your chemistry <?php echo $yourname ?>!  Here is the information that was submitted:</b></p>
<p>
  <ul>
    <li><b>Instructor</b>:&nbsp;<?php echo $teacherName ?></li>
    <li><b>Page</b>:&nbsp;<?php echo $page ?></li>
    <li><b>Total</b>:&nbsp;<?php echo $total ?></li>
    <li><b>Correct</b>:&nbsp;<?php echo $correct ?></li>
    <li><b>Verify</b>:&nbsp;<?php echo $verify ?></li>
    <li><b>Time</b>:&nbsp;<?php echo $time ?></li>
    <li><b>Date/Time</b>:&nbsp;<?php echo $date ?></li>
  </ul>
</p>
</body>
</html>


