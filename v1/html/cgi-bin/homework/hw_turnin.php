<html>
<head>
<title>Chemistry Homework Submission</title>
<script>
function teacherClick(count) {
  id = document.getElementById('instructor').value;
  if (id == '') {
    showDescription('s0', count);
  } else {
    showDescription(id, count);
  }
}

function showDescription(id, count) {
  var i;
  var index;
  for (i=0; i<count; i++) {
    index = 's'+i;
    if (id != index) {
      document.getElementById(index).style.display = "none";
    } else {
      document.getElementById(index).style.display = "block";
    }
  }
}
</script>
<?php
  include 'dbconnect.inc.php';
  $count = 0;
  $sql = "SELECT * FROM teachers ORDER BY Name";
  $teachers = @mysql_query($sql);
  $teacherOptionList = "";
  $teacherIDList = "";
  while ($teacher = @mysql_fetch_array($teachers)) {
    $zangleID = $teacher['ZangleID'];
    $teacherOptionList .= "<option value=\"s" . $count . "\">" . $teacher['Name'] . "</option>\r\n";
    $teacherIDList .= "<input type=\"hidden\" name=\"h$count\" id=\"z$count\" value=\"$zangleID\" />\r\n";

	$sql = "SELECT * FROM students ORDER BY LastName, FirstName";
//    $sql = "SELECT lop.lop_students.LastName, 
//        lop.lop_students.FirstName, 
//        lop.lop_students.StuID, 
//        lop.lop_schedule.Period 
//      FROM lop.lop_students 
//      JOIN lop.lop_schedule 
//        ON lop.lop_students.StuID=lop.lop_schedule.StuID 
//      WHERE lop.lop_schedule.TeacherID=\"$zangleID\"
//      ORDER BY LastName, FirstName";
    $students = @mysql_query($sql);
    $studentOptionList[$count] = "";
    while ($student = @mysql_fetch_array($students)) {
      $studentOptionList[$count] .= "<option value=\"" . $student['StuID'] . "\">" . $student['LastName'] . ", " . 
        $student['FirstName'] . "</option>\r\n";
    }
    $sList .= "<span id=\"s$count\"><p>Your Name: <select name=\"stuid$count\">" . 
      $studentOptionList[$count] . "</select></p></span>\r\n";    
    $count++;
  }  
?>
</head>
 
<body bgcolor=white text=black link=blue alink=blue vlink="#0000BB" onload="teacherClick(<?php echo $count; ?>);">
<font face=arial,helvetica>
<h3>Enter Your name and Select Your Instructor</h3>
To finish submitting your homework, please enter your name and then choose the 
appropriate instructor from the list below:<br>
<br></font>
<form method="POST" action="homework_processor.php">

<p>Your Instructor: <select name="instructor" id="instructor" onchange="teacherClick(<?php echo $count; ?>);"><?php echo $teacherOptionList; ?></select></p>

<?php 
  echo $teacherIDList;
  echo $sList; 
?>

<input type="submit" value=" Submit! "> <input type="reset" value=" Reset ">
<?php
  $correct = $_POST['correct'];
  $page = $_POST['page'];
  $verify = $_POST['verify'];
  $total = $_POST['total'];
  $results = $_POST['results'];
  echo "<input type=\"hidden\" id=\"correct\" name=\"correct\" value=\"$correct\" />\r\n";
  echo "<input type=\"hidden\" id=\"page\" name=\"page\" value=\"$page\" />\r\n";
  echo "<input type=\"hidden\" id=\"verify\" name=\"verify\" value=\"$verify\" />\r\n";
  echo "<input type=\"hidden\" id=\"total\" name=\"total\" value=\"$total\" />\r\n";
  echo "<input type=\"hidden\" id=\"value\" name=\"value\" value=\"$value\" />\r\n";
?>
</form>

</body>
</html>
