function do_js_beautify(content, tabsize) {
	var js_source = content.replace(/^\s+/, '');
	var tabchar = ' ';
	if (tabsize == 1) {
		tabchar = '\t';
	}
	if (js_source && js_source.charAt(0) === '<') {
		var output = style_html(js_source, tabsize, tabchar, 80);
	} else {
		var output = js_beautify(js_source, tabsize, tabchar);
	}
	return output;
}

function pack_js(base64, input) {
	var packer = new Packer;
	if (base64) {
		var output = packer.pack(input, 1, 0);
	} else {
		var output = packer.pack(input, 0, 0);
	}
	return output;
}
function spliter() {
	return true;
}