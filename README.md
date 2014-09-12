mitmproxy-scripts
=================

**Unofficial** scripts developed for use with the [mitmproxy](https://github.com/mitmproxy) project.
<br>

Features requests/issues are welcome!


<h4>Scripts list</h4>
<dl>
<dt>dump_headers.py
</dt>
<dd>Dumps the flow headers (with their respective values) inside the file "headers", written in your current work folder (the one you where when the mitmproxy tool was called).
</dd>
<dt>dump_content.py
</dt>
<dd>Dumps the flow content in a file. It will create a directory called "content" and a subdirectorie for the content-type. Inside this folder it will put the content retrieved, in a file named after it's *sha1* hash and a part of the content-type.
<br><br>
Lets say you made a request and it returned a gif image. It's content-type will be "image/gif". As you will see, the image will be created as <i>"content/image_gif/$sha1oftheimage_gif"</i>. An HTML page will be created as <i>"content/text_html/$sha1ofthepagesource_html"</i>

</dd>
</dl>
