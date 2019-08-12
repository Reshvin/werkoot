function fileOne(input){
    if (input.files && input.files[0]){
        let reader = new FileReader();
        reader.onload = function(e) {
            $('#fileOneImg').attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0])
    } else {
        $('#fileOneImg').attr('src', 'http://werkoot.s3.amazonaws.com/photo_example_picture1.jpg')
    }
}

function fileTwo(input){
    if (input.files && input.files[0]){
        let reader = new FileReader();
        reader.onload = function(e) {
            $('#fileTwoImg').attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0])
    } else {
        $('#fileTwoImg').attr('src', 'http://werkoot.s3.amazonaws.com/photo_example_picture2.jpg')
    }
}

function fileThree(input){
    if (input.files && input.files[0]){
        let reader = new FileReader();
        reader.onload = function(e) {
            $('#fileThreeImg').attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0])
    } else {
        $('#fileThreeImg').attr('src', 'http://werkoot.s3.amazonaws.com/photo_example_picture3.jpg')
    }
}

function viewProfileImage(input){
    if (input.files && input.files[0]){
        let reader = new FileReader();
        reader.onload = function(e) {
            $('#profile_image_placeholder').attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0])
    } else {
        $('#profile_image_placeholder').attr('src', 'https://www.fwhealth.org/wp-content/uploads/2017/03/placeholder-500x500.jpg')
    }
}

function viewNewImage(input){
    if (input.files && input.files[0]){
        let reader = new FileReader();
        reader.onload = function(e) {
            $('#new_image_placeholder').attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0])
    } else {
        $('#new_image_placeholder').attr('src', 'https://www.fwhealth.org/wp-content/uploads/2017/03/placeholder-500x500.jpg')
    }
}


// Password Strenght

function check_pass(){
    const pass = document.getElementById("pass").value;
    const result = document.getElementById("passResult");
    if (pass.length == 0){
      result.innerHTML = ''  
    } else if (pass.length <= 6){
      result.innerHTML = "Password is Weak!!"
    } else if (pass.length <= 9){
      result.innerHTML = "Password is Medium!!"
    } else if (pass.length <= 12){
      result.innerHTML="Password is Strong!!"
    }
  
  }
  




function changeUnits(){
    if ($('#changeUnit').text() === "Convert to inches"){
        measCM = parseFloat($('#measurement').text())
        measIn = measCM * 0.39
        measIn = measIn.toFixed(1)
        $('#measurement').text(measIn)
        $('#unit').text('in')
        $('#changeUnit').text("Convert to centimeters")
    } else {
        $('#measurement').text(measCM)
        $('#unit').text('cm')
        $('#changeUnit').text("Convert to inches")
    }
}

$(document).on('click', '#changeUnit', changeUnits)

