if (typeof payone == 'undefined')
	var payone = {};

payone.client = (function() {
	function ajax(method, data, options)
	{
		var _data = $.extend({}, data || {}, options && options.data || {}, {
			request: method
		});
		var _options = $.extend(options || {}, {
			data: _data,
			dataType: 'jsonp',
			jsonp: 'callback_method',
			url: 'https://secure.pay1.de/client-api/'
		});
		$.ajax(_options);
	}
	
	return {
		ajax: ajax
	};
})();

