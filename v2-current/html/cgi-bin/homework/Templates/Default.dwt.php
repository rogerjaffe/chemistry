<?php session_start(); ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<!-- TemplateBeginEditable name="doctitle" -->
<title>PHHS Web Information System</title>
<!-- TemplateEndEditable --><!-- TemplateBeginEditable name="head" --><!-- TemplateEndEditable -->
<link href="chemistry.css" rel="stylesheet" type="text/css" />
<style>
@media print { DIV.PAGEBREAK {page-break-after: always}}
</style>
<!-- TemplateBeginEditable name="onLoad" -->
<!-- TemplateEndEditable -->
</head>

<body>

<strong>Patrick Henry Chemistry Practice</strong><br />
<!-- TemplateBeginEditable name="PageTitle" -->View Student Results<!-- TemplateEndEditable --><br />
<?php
// Begin authorization test
  include '../../../../includes/userSession.php';
  include_once 'dbconnect.inc.php'; 
  $userSession = new userSession($dbcnx);
  $userSession->validateSession($_SESSION['sessionID'], $sessionVariables);
  if ($sessionVariables['Chemistry']['Authenticate']) {
?>

<a href="index.php">Home</a><br />
<!-- TemplateBeginEditable name="Content" -->
<p>Content</p>
<!-- TemplateEndEditable -->
<?php
  } else {
    echo "<p><font color=\"#FF0000\"><b>You are not authorized for this system</b></font></p>";
  }
?>
<p class="small_font">Patriot Internet Information System <br />
Copyright 2008 Roger Jaffe<br />
Version <?php echo $config['Version']; ?></p>
</body>
</html>
