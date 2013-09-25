// Idea from http://jsbin.com/eyotuz/3/edit,
//           http://stackoverflow.com/a/16423486/5056
//

var isMouseMoveNotDrag = false

// $(document).on('mousemove', detectMouse);

function detectMouse(e) {
  if(e.which || e.button)
    return;
  isMouseMoveNotDrag = true;
  mouseMoveStateChanged()
  $('#mouseOrNot').text("Mouse Detected!");
  $(document).off('mousemove', detectMouse);
}
