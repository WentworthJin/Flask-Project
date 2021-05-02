function create_class(){
  var class_name = document.getElementById("class1").value;
  var var1 = document.getElementById("property1").value;
  var property1 = document.getElementById("property1-1").value;
  var var2 = document.getElementById("property2").value;
  var property2 = document.getElementById("property2-2").value;
  var var3 = document.getElementById("property3").value;
  var property3 = document.getElementById("property3-3").value;

  if (class_name == ""){
    alert("You did not enter any class name");
  }
  if (var1 == "" || var2 == "" || var3 == ""){
    alert("You did not enter some variable names");x
  }
  if (property1 == "" || property2 == "" || property3 == ""){
    alert("You did not enter some variable types");
  }

  else{
    document.getElementById('class_sample').style.display = "block";
    document.getElementById('class_value').innerHTML = class_name;
    document.getElementById('var1_value').innerHTML = var1;
    document.getElementById('property1_value').innerHTML = property1;
    document.getElementById('var2_value').innerHTML = var1;
    document.getElementById('property2_value').innerHTML = property1;
    document.getElementById('var3_value').innerHTML = var1;
    document.getElementById('property3_value').innerHTML = property1;
    document.getElementById('class_output').innerHTML = class_name;
  }
}

function clearclass(){
  document.getElementById("class1").value = '';
  document.getElementById("property1").value = '';
  document.getElementById("property1-1").value = '';
  document.getElementById("property2").value = '';
  document.getElementById("property2-2").value = '';
  document.getElementById("property3").value = '';
  document.getElementById("property3-3").value = '';
  document.getElementById('class_sample').style.display = "none";
  alert("You have cleared your class")
}

function show_int_array(){
  document.getElementById('array_result').innerHTML = "<pre>var someInts:[Int] = [10, 20, 30]</pre>";
}

function show_str_array(){
  document.getElementById('array_result').innerHTML = "<pre>var someStrings: [String] = [\"Eggs\", \"Milk\"]</pre>";
}

function accept_str(){
  document.getElementById('second_example').innerHTML = "\
  <pre>func swapTwoStrs(_ a: inout String, _ b: inout String) {\nlet temporaryA = a\na = b\nb = temporaryA\n}\n<b class=\"yewp\">! This function only accepts String values</b></pre>";
}

function accept_double(){
  document.getElementById('second_example').innerHTML = "\
  <pre>func swapTwoDoubles(_ a: inout Double, _ b: inout Double) {\nlet temporaryA = a\na = b\nb = temporaryA\n}\n<b class=\"yewp\">! This function only accepts Double values</b></pre>";
}

function accept_int(){
  document.getElementById('second_example').innerHTML = "\
  <pre>func swapTwoInts(_ a: inout Int, _ b: inout Int) {\nlet temporaryA = a\na = b\nb = temporaryA\n}\n<b class=\"yewp\">! This function only accepts Integer values</b></pre>";
  document.getElementById('alert_1').innerHTML = "Not efficient, Time-consuming !"
}