var folder = '/';
var server = get_server_path() + folder;

$(window).load(function(){
	var page = get_currentpage();
	var last_item = getLastItem(page)
	
	load_turnon()
	display_submenu()

	if(last_item.length && $('#'+last_item).length) gotoTop(last_item)	

	if($('.slider').length) load_cycle_slider()

	if($('.grid_slider').length) load_grid_slider()

	if($('#form_contact').length) load_form_contact();
	
});

function load_form_contact()
{
	$('#form_contact').submit(function()
	{
		var flag = true;
		var tags = new Array('name', 'email', 'mensaje');
		var active_lang = $('#language').find('.active');
		var lang = $(active_lang).text() == 'Esp' ? 0:1;
		var msg_fill_fields = new Array('Favor de llenar campos marcados en rojo', 'Plase fill all fields in red');
		var msg_valid_email = new Array('Favor de captura un email correcto.', 'Please put a valid email.');
		var msg_sending = new Array('Enviando mensaje, Favor espera...', 'Sending message, please waite...');
		var msg_success = new Array('Mensaje enviado correctamente, gracias.', 'Your message has been sent, thank you.');
		var msg_error = new Array('Lo sentimos el mensaje no se pudo enviar, favor de intetar mas tarde.', 'We are sorry, the message could not been sent, please try later.');
		for(i=0; i<tags.length; i++)
		{
			if($('#'+tags[i]).val() == '')
			{
				flag = false;
				$('#'+tags[i]).prev().addClass('missed');
			}
			else $('#'+tags[i]).prev().removeClass('missed');
		}
		if(!flag) $('#msg').text(msg_fill_fields[lang]);
		else
		{
			if(!is_email($('#email').val())) $('#msg').text(msg_fill_fields[lang]);
			else
			{
				$('#msg').text(msg_sending[lang]);
				$.post("send_mail_form", $("#form_contact").serialize(), function(data){
					if(data == 'success')
					{
						$('#msg').text(msg_success[lang]); 
						clear_form('form_contact');
					}
					else if(data == 'empty_data') $('#msg').text(msg_fill_fields[lang]);
					else $('#msg').text(msg_error[lang]);
				})
			}
		}
		return false;
	})
}

function clear_form(form)
{
	$( '#'+form ).each(function(){
	    this.reset();
	});
}
function is_email(email)
{
	var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function display_submenu()
{
	$('ul.menu li').hover(function() {
        $(this).find('.invisible').show();
    },
    function() {
      $(this).find('.invisible').hide();
	});
}

function load_grid_slider()
{
	var parent = '';
	var slider = '';
	$('.grid li').click(function(){
		id = $(this).attr('id');
		if(id.length)
		{
			parent = $(this).parents()
			parent = parent[0]

			console.log(parent) 
			console.log(slider)
			slider = $(parent).attr('alt');

			$(parent).find('.current').removeClass('current')
			$(this).addClass('current')
			$('#'+slider).find('.current').removeClass('current');
			$('#'+slider).find('#item_'+id).addClass('current');
		}
		return false;
	})
	$('.slider_navigation li').click(function(){
		slider = $(this).parent().attr('alt')
		element = $('#'+slider).find('.current')
		if($(this).hasClass('next'))
		{
			if(!$(element).hasClass('last'))
			{
				$(element).removeClass('current')
				$(element).next().addClass('current')
				set_current_grid(slider, $(element).next().attr('id'))
			}
			else{
				$(element).removeClass('current')
				$('#'+slider).find('.first').addClass('current')
				set_current_grid(slider, $('#'+slider).find('.first').attr('id'))
			}
		}else if($(this).hasClass('prev')){
			if(!$(element).hasClass('first'))
			{
				$(element).removeClass('current')
				$(element).prev().addClass('current')
				set_current_grid(slider, $(element).prev().attr('id'))
			}
			else{
				$(element).removeClass('current')
				$('#'+slider).find('.last').addClass('current')
				set_current_grid(slider, $('#'+slider).find('.last').attr('id'))
			}
		}
		return false	
	})
}

function set_current_grid(slider, id)
{
	id = id.replace('item_', '');
	$('#grid_'+slider).find('.current').removeClass('current')
	$('#grid_'+slider).find('#'+id).addClass('current')
}

function load_cycle_slider()
{
	
}

function load_turnon(){
	$('#wrapper').animate({
		'opacity': '1'
		}, 'slow'
	);
}

function isValidEmailAddress(emailAddress) {
    var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
    return pattern.test(emailAddress);
}

function get_currentpage(){
	var loc = window.location;
	p = loc.href.substring(loc.href.indexOf(loc.host) + loc.host.length + folder.length );
	if(p == '') p = 'inicio';
	return p;
}

function gotoTop(id){
	if(id.length)
		$('html, body').animate({
			scrollTop: $('#'+id).offset().top - 100
		}, 1250);
}

function getLastItem(cadena){
       var params = cadena.split('/');
       return params.pop();
}

function get_server_path(){
	var loc = window.location;
	return "http://" + loc.hostname;
}