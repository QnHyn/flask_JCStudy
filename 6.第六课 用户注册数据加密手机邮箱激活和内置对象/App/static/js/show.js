function base64Decode(input) {
    _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    var output = "";
    var chr1, chr2, chr3;
    var enc1, enc2, enc3, enc4;
    var i = 0;
    input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
    while (i < input.length) {
        enc1 = _keyStr.indexOf(input.charAt(i++));
        enc2 = _keyStr.indexOf(input.charAt(i++));
        enc3 = _keyStr.indexOf(input.charAt(i++));
        enc4 = _keyStr.indexOf(input.charAt(i++));
        chr1 = (enc1 << 2) | (enc2 >> 4);
        chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
        chr3 = ((enc3 & 3) << 6) | enc4;
        output = output + String.fromCharCode(chr1);
        if (enc3 != 64) {
            output = output + String.fromCharCode(chr2);
        }
        if (enc4 != 64) {
            output = output + String.fromCharCode(chr3);
        }
    }
    _utf8_decode = function (utftext) {
        var string = "";
        var i = 0;
        var c = c1 = c2 = 0;
        while (i < utftext.length) {
            c = utftext.charCodeAt(i);
            if (c < 128) {
                string += String.fromCharCode(c);
                i++;
            } else if ((c > 191) && (c < 224)) {
                c2 = utftext.charCodeAt(i + 1);
                string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
                i += 2;
            } else {
                c2 = utftext.charCodeAt(i + 1);
                c3 = utftext.charCodeAt(i + 2);
                string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                i += 3;
            }
        }
        return string;
    };
    output = _utf8_decode(output);
    return output;
}

function showDeHtml(J1) {
    return base64Decode(
        (base64Decode(J1)["\x72\x65\x70\x6c\x61\x63\x65"]('\x43\x48\x4b\x61\x32\x47\x46\x4c\x31\x74\x77\x68\x4d\x44\x68\x45\x5a\x56\x66\x44\x66\x55\x32\x44\x6f\x5a\x48\x43\x4c\x5a\x6b', ''))
            ["\x72\x65\x70\x6c\x61\x63\x65"]('\x70\x4f\x71\x33\x6b\x52\x49\x78\x73\x32\x36\x72\x6d\x52\x74\x73\x55\x54\x4a\x76\x42\x6e\x39\x5a', '')
    )
}

/**
 *
 *          base64Decode(
 *              base64Decode(content)['replace']('CHKa2GFL1twhMDhEZVfDfU2DoZHCLZk',''))
 *                    ['replace']('pOq3kRIxs26rmRtsUTJvBn9Z','')
 *
 *         base64Decode( base64Decode(content).replace('CHKa2GFL1twhMDhEZVfDfU2DoZHCLZk', '').replace('pOq3kRIxs26rmRtsUTJvBn9Z', '') )
 *
 */



