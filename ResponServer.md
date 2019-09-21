# Kode Respon Status HTTP

**Sukses**

```
200 OK
201 Request Berhasil dibuat
202 Request berhasil diterima
203 Non-Authoritative Information (since HTTP/1.1)
204 Tanpa Konten
205 Reset Content
206 Partial Content
207 Multi-Status (WebDAV; RFC 4918)
208 Already Reported (WebDAV; RFC 5842)
226 IM Used (RFC 3229)
```

**Pengalihan**

```
300 Multiple Choices
301 Dipindah Permanen
302 Ditemukan
303 Lihat Lainnya
304 Not Modified
305 Use Proxy (since HTTP/1.1)
306 Switch Proxy
307 Temporary Redirect (since HTTP/1.1)
308 Permanent Redirect (Experimental RFC; RFC 7238)
```

**Kesalahan Dari Klien**

```
400 Permintaan Tak Layak
401 Unauthorized
402 Payment Required
403 Terlarang
404 Tidak Ditemukan
405 Method Not Allowed
406 Not Acceptable
407 Proxy Authentication Required
408 Request Timeout
409 Conflict
410 Tidak tersedia
411 Length Required
412 Precondition Failed
413 Request Entity Too Large
414 Request-URI Too Long
415 Unsupported Media Type
416 Requested Range Not Satisfiable
417 Expectation Failed
419 Authentication Timeout (not in RFC 2616)
420 Method Failure (Spring Framework)
```

**Kesalahan Server**

```
500 Internal Server Error
501 Not Implemented
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
505 HTTP Version Not Supported
506 Variant Also Negotiates (RFC 2295)
507 Insufficient Storage (WebDAV; RFC 4918)
508 Loop Detected (WebDAV; RFC 5842)
509 Bandwidth Limit Exceeded (Apache bw/limited extension)
510 Not Extended (RFC 2774)
511 Network Authentication Required (RFC 6585)
520 Origin Error (CloudFlare)
521 Web server is down (CloudFlare)
522 Connection timed out (CloudFlare)
523 Proxy Declined Request (CloudFlare)
524 A timeout occurred (CloudFlare)
598 Network read timeout error (Unknown)
599 Network connect timeout error (Unknown)
```
