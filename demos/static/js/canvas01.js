var canvas = new fabric.Canvas('canvas', {
    isDrawingMode: true
});
fabric.Object.prototype.transparentCorners = false;
canvas.freeDrawingBrush = new fabric['PencilBrush'](canvas);
canvas.freeDrawingBrush.color = "black";
canvas.freeDrawingBrush.width = 18;

function canvas_clear() {
    canvas.clear();
    $("#resultbase64").val('');
}

function canvas_to_base64() {
    $("#resultbase64").val(canvas.toDataURL("image/jpeg"));
}
