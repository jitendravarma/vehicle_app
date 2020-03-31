var csrfval = $('input[name="csrfmiddlewaretoken"]').val();

$(document).on('click', '.delete-profile', function () {
    var value = $('#vehicle-id').val();
    if (value !== "" || value !== undefined) {
        $.ajax({
            cache: false,
            url: "/vehicle/delete/",
            type: "POST",
            data: { 'id': value },
            headers: { 'X-CSRFToken': csrfval },
            success: function (data) {
                if (data.msg == "success") {
                    $('.alert-row-error').removeAttr('hidden');
                    setTimeout(function () { window.location.href = '/home' }, 5000);
                }
            },
        });
    }
});