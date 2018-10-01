$(document).ready(function(){
	var ShowForm = function(){
		var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function() {
                $('#usermodal').modal('show');
            },
            success: function(data) {
                $('#usermodal .modal-content').html(data.html_form);
            }
        });
    };


    var SaveForm =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
				    $('#usertable tbody').html(data.profile);
					$('#usermodal').modal('hide');

				} else {
					$('#usermodal .modal-content').html(data.html_form)
				}
			}
		});
		return false;
	};



$('#usertable').on("click",'.show-form-update',ShowForm);
$('#usermodal').on("submit",'.update-form',SaveForm)
});