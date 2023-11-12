$tools = ['curl', 'git', 'wget']

$restricted_extras = ['ttf-mscorefonts-installer', 'rar', 'unrar', 'libavcodec-extra', 'gstreamer1.0-libav', 'gstreamer1.0-plugins-ugly', 'gstreamer1.0-vaapi']

$fonts = ['fonts-crosextra-carlito', 'fonts-crosextra-caladea']

package { $tools:
  ensure => 'installed',
}

package { $restricted_extras:
  ensure => 'installed',
}

package { $fonts:
  ensure => 'installed',
}
