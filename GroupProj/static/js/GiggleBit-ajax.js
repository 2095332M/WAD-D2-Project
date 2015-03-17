
function clicked_liked() {
  var imgid;
  var usrid;
  var likes;
  imgid = $('#likes').attr("data-imgid");
  usrid = $('#likes').attr("data-userid");
  likes = $('#likes').attr("data-likes");
  $.get('/gigglebit/like_category/', {image_id: imgid , user_id:usrid, likes_num:likes}, function(likes_count){
    $('#like_count').html(likes_count);
    $('#likes').hide();
})}
