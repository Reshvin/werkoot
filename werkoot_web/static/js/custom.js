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
  



