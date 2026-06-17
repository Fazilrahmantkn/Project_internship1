function showName(){
	nameResult.innerHTML='Student Name: '+studentName.value;
}
function checkAge(){
	ageResult.innerHTML=age.value>=18?'Eligible for College Admission':'Not Eligible';
}
function addNumbers(){
	addResult.innerHTML='Result: '+(Number(num1.value)+Number(num2.value));
}
function calculateMarks(){
	marksResult.innerHTML='Total: '+(Number(eng.value)+Number(math.value)+Number(sci.value));
}
function greetStudent(){
	greetResult.innerHTML='Welcome to Student Management System';
}
function changeText(){
	title.innerHTML='Welcome Students';
}
function changeColor(c){
	document.body.style.backgroundColor=c;
}
function checkEvenOdd(){
	evenOddResult.innerHTML=(Number(evenOdd.value)%2===0)?'Even Number':'Odd Number';
}
function calculateGrade(){
	let m=Number(gradeMarks.value);gradeResult.innerHTML=m>=90?'A':m>=80?'B':m>=70?'C':'D';
}
function markAttendance(){
	attendanceResult.innerHTML='Attendance Marked Successfully';attendanceResult.style.color='green';
}
function countCharacters(){
	charResult.innerHTML='Characters: '+charInput.value.length;
}
function showStudentInfo(){
	infoResult.innerHTML='<h3>Student Information</h3>Name: '+infoName.value+'<br>Roll No: '+roll.value+'<br>Course: '+course.value;
}
function convertTemperature(){
	tempResult.innerHTML='Fahrenheit: '+((Number(celsius.value)*9/5)+32);
}
function togglePassword(){
	password.type=password.type==='password'?'text':'password';
}
function registerStudent(){
	regResult.innerHTML='<h3>Registration Successful</h3>Name: '+regName.value+'<br>Age: '+regAge.value+'<br>Course: '+regCourse.value;
}
function calculateTotal(a,b,c){
	return a+b+c;
}
function calculateResult(){
	let t=calculateTotal(Number(m1.value),Number(m2.value),Number(m3.value));let p=t/3;let g=p>=90?'A':p>=80?'B':p>=70?'C':'D';labResult.innerHTML='Student Name: '+labName.value+'<br>Total Marks: '+t+'<br>Grade: '+g;
}
