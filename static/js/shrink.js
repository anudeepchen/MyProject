
   
document.getElementById("howitworksbutton").onclick = function () {
        location.href = "/howitworks";
};


$(document).ready(function(){
$('#employeebutton').click(function(){
       $('#howitworks-emp').slideToggle(400);
});       
});

$('#cloud-button').click(function(){
       $('#cloud-block').slideToggle(400);
       $('html, body').animate({scrollTop: 1600}, "slow");
       
       $('#api-button').click(function() {
       $('#cloud-block').slideUp(300);
});
       $('#tech-button').click(function() {
       $('#cloud-block').slideUp(300);
});
       $('#ml-button').click(function() {
       $('#cloud-block').slideUp(300);
});
    });
    
    $('#close-button').click(function(){
       $('#api-block').slideUp(300);
        $('#cloud-block').slideUp(300);
         $('#tech-block').slideUp(300);
         $('#ml-block').slideUp(300);
    });
    
    
   $('#api-button').click(function(){
        $('#api-block').slideToggle(400);
       $('html, body').animate({scrollTop: 1600}, "slow");
        $('#cloud-button').click(function() {
        $('#api-block').slideUp(300);
});
       $('#tech-button').click(function() {
       $('#api-block').slideUp(300);
});
       $('#ml-button').click(function() {
       $('#api-block').slideUp(300);
});
    });
   
   
   $('#tech-button').click(function(){
        $('#tech-block').slideToggle(400);
       $('html, body').animate({scrollTop: 1600}, "slow");
       
        $('#cloud-button').click(function() {
        $('#tech-block').slideUp(300);
});
       $('#api-button').click(function() {
       $('#tech-block').slideUp(300);
});
       $('#ml-button').click(function() {
       $('#tech-block').slideUp(300);
});
    });
   
   
   $('#ml-button').click(function(){
        $('#ml-block').slideToggle(400);
       $('html, body').animate({scrollTop: 1600}, "slow");
        $('#cloud-button').click(function() {
        $('#ml-block').slideUp(300);
});
       $('#tech-button').click(function() {
       $('#ml-block').slideUp(300);
});
       $('#api-button').click(function() {
       $('#ml-block').slideUp(300);
});
    });
  

 