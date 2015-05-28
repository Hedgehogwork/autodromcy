/**
 * Created by semyon on 14.04.15.
 */
$('#more-option-open').on('click',function(){
    $(this).hide();
    $('.add-option').show();
});
$('#more-option-close').on('click',function(){
    $('.add-option').hide();
    $('#more-option-open').show();
});
$('.car-dody-style').on('change','select',function(){
/*
console.log(($(this).val()));
    var array_body = $(this).val();
    console.log(array_body);
    if ("any" in array_body) {
        console.log('!!!!!!!!!!!!!!!!');
    }
//    if(this.val=='')
*/

});
   $('#search-bay-car').on('click',function(){
      window.location = "/searchresalt.html";
   });

$(document).delegate('*[data-toggle="lightbox"]', 'click', function(event) {
    event.preventDefault();
    $(this).ekkoLightbox();
});

$('#showtel').on('click',function() {

    $(this).find('span').text( $(this).data('last') );

});