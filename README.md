# clear_chrome_cache_ramdisk
<h3><b>Что это за проект?</b></h3>
<p>Данный проект, создан для очистки кеша браузера от google chrome, из-за проблем данного браузера для пользователей которые используют SSD накопители!</p>
<h3><b>Что требуется для проекта?</b></h3>
<p>Для <b>Windows</b> пользователей, требуется:</p>
<p><a href="https://www.python.org/downloads/release">python 3</a></p>
<p><a href="http://memory.dataram.com/products-and-services/software/ramdisk">ramdisk</a> - условно-бесплатная</p>
<p>Для <b>Linux</b> пользователей, требуется:</p>
<p>python3</p>
<p>Для Windows и Linux:</p>
<pre>
<code>pip install psutil</code>
<code>pip install schedule - для linux, существует аналог cron</code>
</pre>
<h3><b>Как настроить проект?</b></h3>
<p><b>Для Windows:</b></p>
<p>Устанавливаем ramdisk:</p>
<ul>
<li>Basic settings - Disk size - 512 mb или выше;</li>
<li>Load/Save - Image File - RAMDisk.img;</li>
<li>Load Disk Image at Startup - True;</li>
<li>Save Disk Image Now;</li>
<li>Start RAMDisk;</li>
</ul>
<p>На этом этапе настройка ramdisk закончена</p>
<p>Следующим этапом, нужно настроить браузер, для работы с кешом</p>
<p>Для этого нужно указать параметр в ярлыке браузера, параметр:</p>
<pre><code>--disk-cache-dir</code></pre>
<p>Данный параметр позволяет хранить кеш браузера, в отдельном каталоге</p>
<p>Пример использования:</p>
<pre><code>"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --disk-cache-dir="X:\Chrome"</code></pre>
<p>Так же есть параметр:</p>
<pre><code>--user-data-dir</code></pre>
<p>Данный параметр позволяет хранить весь профиль, в отдельном каталоге</p>
<p>Пример использования:</p>
<pre><code>"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --user-data-dir="X:\Chrome"</code></pre>
<p>Настройка закончена для системы windows</p>
<p><b>Для Linux:</b></p>
<p>Для начала нам нужно, создать каталог google_cache_tmpfs</p>
<p><pre><code>mkdir google_cache_tmpfs</code></pre></p>
<p>Затем нужно смонтировать каталог под файловую систему tmpfs</p>
<pre><code>mount -t tmpfs -o size=512m tmpfs google_cache_tmpfs</code></pre>
<p>Альтернативный способ (для постоянной основы)</p>
<p>Нужно в /etc/fstab добавить код:</p>
<pre><code>tmpfs       /path/to/google_cache_tmpfs tmpfs   nodev,nosuid,noexec,nodiratime,size=1024M   0 0</code></pre>
<p>Настройка google chrome делается аналогично как и в Windows</p>
<p>Пример использования:</p>
<pre><code>chrome --disk-cache-dir=/path/to/google_cache_tmpfs</code></pre>
<p>Так же для того чтобы, не писать каждый нужно создать скрипт, например chrome_ramdisk.sh:</p>
<pre><code>touch chrome_ramdisk.sh</code></pre>
<p>С таким содержимым скрипта:</p>
<pre>
<code>#!/bin/sh</code>
<code>chrome --disk-cache-dir=/path/to/google_cache_tmpfs</code>
</pre>
<p>Затем дать права на исполнение команды</p>
<pre><code>сhmod +x chrome_ramdisk.sh</code></pre>
<p>Настройка закончена для системы linux</p>
<p>Альтернативный способ для создания ram диска - <a href="https://habrahabr.ru/post/205158/">Перенос Google Chrome на RAM-диск в Linux</a></p>
<h3><b>Переменные в run.py</b></h3>
<p><b>local_drive</b> - диск или каталог на котором ramdisk</p>
<p><b>path_to_chrome_cache</b> - полный путь к кешу браузера</p>
<p><b>percent_size</b> - процент после которого, будут удаляться файлы из кеша браузера</p>
<p><b>size_in_kb</b> - размер файла, если размер файла больше установленного, чем в переменной, он будет удален</p>
<p><b>check_schedule_in_minutes</b> - как часто проверять кеш в минутах</p>
