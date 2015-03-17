
function clicked_liked() {
  var imgid;
  var usrid;
  imgid = $('#likes').attr("data-imgid");
  usrid = $('#likes').attr("data-userid");
  $.get('/gigglebit/like_category/', {image_id: imgid , user_id:usrid}, function(created){
    if(created){
      $('#likes_count').html($('#likes_count')+1);
    }
    $('#likes').hide();
})}
