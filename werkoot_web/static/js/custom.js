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
