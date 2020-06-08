
//Define calendar(s): addCalendar ("Unique Calendar Name", "Window title", "Form element's name", Form name")
addCalendar("fromdate", "Select Date", "fromdate", "form1");
addCalendar("todate", "Select Date", "todate", "form1");

// default settings for English
// Uncomment desired lines and modify its values
// setFont("arial", 9);
 setWidth(90, 1, 15, 1);
 setColor("#229922", "#229922", "#ffff66", "#ffff99", "#ff9999", "#229922", "#333333");
 setFontColor("#333333", "#333333", "#333333", "#000000", "#333333");
 setFormat("mm/dd/yyyy");
// setSize(200, 200, -200, 16);

// setWeekDay(0);
// setMonthNames("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");
// setDayNames("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");
// setLinkNames("[Close]", "[Clear]");
//
// Usage: onSubmit="return ValidateDate('javascript:checkDate(\'BulletinCalendar\')'
//
function ValidateDate(jsStr) {
  if (eval(jsStr) != 0) {
    alert('Invalid date');
    return (false);
  }
}
