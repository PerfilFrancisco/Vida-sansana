
$("#formulario").submit(function(e) {
    console.log("asdsfgh");
    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var actionUrl = form.attr('action');
    
    $.ajax({
        type: "POST",
        url: actionUrl,
        data: form.serialize(), // serializes the form's elements.
        success: function(data)
        {
            $('#accordionExample').html(data); // show response from the php script.
        }
    });
    
});
function defecto(){
    $.ajax({
        type: "POST",
        url: 'hitodefecto/',
        data: form.serialize(), // serializes the form's elements.
        success: function(data)
        {
            $('#accordionExample').html(data); // show response from the php script.
        }
    });
}