var obj = $("#dragandrophandler");
obj.on('dragenter', function (e) 
{
    e.stopPropagation();
    e.preventDefault();
    $(this).css('border', '2px solid #0B85A1');

});
obj.on('dragover', function (e) 
{
     e.stopPropagation();
     e.preventDefault();
     $("#dragandrophandler").css('background-color', '#ffffe0');
});
obj.on('drop', function (e) 
{
     $(this).css('border', '2px dotted #0B85A1');
     e.preventDefault();
     var file = e.originalEvent.dataTransfer.files[0];
     if(file.type === 'image/jpeg' || file.type === 'image/png') {
         //We need to send dropped files to Server
        const reader = new FileReader()
        reader.onload = () => {
            $("#imgdiv").children('img').attr('src', reader.result);
            $("#resultbase64").val(reader.result);
        }
        reader.readAsDataURL(file);    
        $("#dragandrophandler").css('background-color', '#ffffff');
    } else {
        alert("ドロップできるのは、JPEG・PNG画像ファイルだけです");
    }

});
$(document).on('dragenter', function (e) 
{
    e.stopPropagation();
    e.preventDefault();
    $("#dragandrophandler").css('background-color', '#ffffff');

});
$(document).on('dragover', function (e) 
{
  e.stopPropagation();
  e.preventDefault();
  obj.css('border', '2px dotted #0B85A1');
});
$(document).on('drop', function (e) 
{
    e.stopPropagation();
    e.preventDefault();
});