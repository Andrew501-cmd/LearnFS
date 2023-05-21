from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'api', 'API_LearnFS.urls', name='api'),
    host(r'clientǀwwwǀ ', 'CLIENT_LearnFS.urls', name='client'),
    host(r'game', 'GAME_LearnFS.urls', name='game'),
)