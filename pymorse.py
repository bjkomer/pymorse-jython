


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>morse/bindings/pymorse/src/pymorse/pymorse.py at 40dcaf7c5ae79d72425c88a08339741aba5fab65 · morse-simulator/morse</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png">
    <meta name="hostname" content="github-fe125-cp1-prd.iad.github.net">
    <meta name="ruby" content="ruby 1.9.3p194-tcs-github-tcmalloc (e233cae611) [x86_64-linux]">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035/">
    <link rel="xhr-socket" href="/_sockets" />
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="81612D9F:3B90:2F5F65DF:5266D2D8" name="octolytics-dimension-request_id" /><meta content="1361151" name="octolytics-actor-id" /><meta content="bjkomer" name="octolytics-actor-login" /><meta content="eea386fa2351f8d8a163dd2ffe25e0b9334018d823832d5e9e1d44d2b27f0dab" name="octolytics-actor-hash" />
    

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="hYreSU/zXubuIvDBx8m9YBaBYhv5TKElukDeGAZ3LFU=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-d51331e7bad1e3cc8e0544405a6771bb9662ee08.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-f49856bdb8fc62ed04388081a6a8cfeda7ce1d28.css" media="all" rel="stylesheet" type="text/css" />
    

    

      <script src="https://github.global.ssl.fastly.net/assets/frameworks-8a61e23841d9e5ecc084748ec552e548cd05c977.js" type="text/javascript"></script>
      <script src="https://github.global.ssl.fastly.net/assets/github-0b2bf36f76875f4c575d21c41019255e1149beb8.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="d76045ac556af89052c1357cd97ea058">

        <link data-pjax-transient rel='permalink' href='/morse-simulator/morse/blob/40dcaf7c5ae79d72425c88a08339741aba5fab65/bindings/pymorse/src/pymorse/pymorse.py'>
  <meta property="og:title" content="morse"/>
  <meta property="og:type" content="githubog:gitrepository"/>
  <meta property="og:url" content="https://github.com/morse-simulator/morse"/>
  <meta property="og:image" content="https://github.global.ssl.fastly.net/images/gravatars/gravatar-user-420.png"/>
  <meta property="og:site_name" content="GitHub"/>
  <meta property="og:description" content="morse - The Modular OpenRobots Simulation Engine"/>

  <meta name="description" content="morse - The Modular OpenRobots Simulation Engine" />

  <meta content="4056603" name="octolytics-dimension-user_id" /><meta content="morse-simulator" name="octolytics-dimension-user_login" /><meta content="856780" name="octolytics-dimension-repository_id" /><meta content="morse-simulator/morse" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="856780" name="octolytics-dimension-repository_network_root_id" /><meta content="morse-simulator/morse" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/morse-simulator/morse/commits/40dcaf7c5ae79d72425c88a08339741aba5fab65.atom" rel="alternate" title="Recent Commits to morse:40dcaf7c5ae79d72425c88a08339741aba5fab65" type="application/atom+xml" />

  </head>


  <body class="logged_in  env-production linux vis-public  page-blob">
    <div class="wrapper">
      
      
      


      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    
    <a href="/notifications" class="notification-indicator tooltipped downwards" data-gotokey="n" title="You have unread notifications">
        <span class="mail-status unread"></span>
</a>

      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    data-username="bjkomer"
      data-repo="morse-simulator/morse"
      data-branch="40dcaf7c5ae79d72425c88a08339741aba5fab65"
      data-sha="c6303abd70ce239b849dca9116446bc6a6d2e1b4"
  >

    <input type="hidden" name="nwo" value="morse-simulator/morse" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    


  <ul id="user-links">
    <li>
      <a href="/bjkomer" class="name">
        <img height="20" src="https://2.gravatar.com/avatar/6afdd7499bf9239f401c06bc31fd98ad?d=https%3A%2F%2Fidenticons.github.com%2F1432f2a74843e697d34955eb3001c63e.png&amp;s=140" width="20" /> bjkomer
      </a>
    </li>

      <li>
        <a href="/new" id="new_repo" class="tooltipped downwards" title="Create a new repo" aria-label="Create a new repo">
          <span class="octicon octicon-repo-create"></span>
        </a>
      </li>

      <li>
        <a href="/settings/profile" id="account_settings"
          class="tooltipped downwards"
          aria-label="Account settings "
          title="Account settings ">
          <span class="octicon octicon-tools"></span>
        </a>
      </li>
      <li>
        <a class="tooltipped downwards" href="/logout" data-method="post" id="logout" title="Sign out" aria-label="Sign out">
          <span class="octicon octicon-log-out"></span>
        </a>
      </li>

  </ul>

<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>



    <li class="section-title">
      <span title="morse-simulator/morse">This repository</span>
    </li>
      <li>
        <a href="/morse-simulator/morse/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
</ul>

</div>


    
  </div>
</div>

      

      




          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="hYreSU/zXubuIvDBx8m9YBaBYhv5TKElukDeGAZ3LFU=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="856780" />

    <div class="select-menu js-menu-container js-select-menu">
      <a class="social-count js-social-count" href="/morse-simulator/morse/watchers">
        14
      </a>
      <span class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0">
        <span class="js-select-button">
          <span class="octicon octicon-eye-watch"></span>
          Watch
        </span>
      </span>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for discussions in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
  
<div class="js-toggler-container js-social-container starring-container ">
  <a href="/morse-simulator/morse/unstar" class="minibutton with-count js-toggler-target star-button starred upwards" title="Unstar this repo" data-remote="true" data-method="post" rel="nofollow">
    <span class="octicon octicon-star-delete"></span><span class="text">Unstar</span>
  </a>
  <a href="/morse-simulator/morse/star" class="minibutton with-count js-toggler-target star-button unstarred upwards" title="Star this repo" data-remote="true" data-method="post" rel="nofollow">
    <span class="octicon octicon-star"></span><span class="text">Star</span>
  </a>
  <a class="social-count js-social-count" href="/morse-simulator/morse/stargazers">68</a>
</div>

  </li>


        <li>
          <a href="/morse-simulator/morse/fork" class="minibutton with-count js-toggler-target fork-button lighter upwards" title="Fork this repo" rel="facebox nofollow">
            <span class="octicon octicon-git-branch-create"></span><span class="text">Fork</span>
          </a>
          <a href="/morse-simulator/morse/network" class="social-count">38</a>
        </li>


</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/morse-simulator" class="url fn" itemprop="url" rel="author"><span itemprop="title">morse-simulator</span></a>
          </span>
          <span class="repohead-name-divider">/</span>
          <strong><a href="/morse-simulator/morse" class="js-current-repository js-repo-home-link">morse</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">

      <div class="repository-with-sidebar repo-container ">

        <div class="repository-sidebar">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped leftwards" title="Code">
        <a href="/morse-simulator/morse" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /morse-simulator/morse">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped leftwards" title="Issues">
          <a href="/morse-simulator/morse/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /morse-simulator/morse/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>65</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped leftwards" title="Pull Requests"><a href="/morse-simulator/morse/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /morse-simulator/morse/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>2</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped leftwards" title="Wiki">
          <a href="/morse-simulator/morse/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_wiki /morse-simulator/morse/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/morse-simulator/morse/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /morse-simulator/morse/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/morse-simulator/morse/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /morse-simulator/morse/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/morse-simulator/morse/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /morse-simulator/morse/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

            <div class="only-with-full-nav">
              

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/morse-simulator/morse.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/morse-simulator/morse.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><strong>SSH</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="git@github.com:morse-simulator/morse.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="git@github.com:morse-simulator/morse.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/morse-simulator/morse" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/morse-simulator/morse" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="octicon help tooltipped upwards" title="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>



              <a href="/morse-simulator/morse/archive/40dcaf7c5ae79d72425c88a08339741aba5fab65.zip"
                 class="minibutton sidebar-button"
                 title="Download this repository as a zip file"
                 rel="nofollow">
                <span class="octicon octicon-cloud-download"></span>
                Download ZIP
              </a>
            </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:e83bcf1fe4a21e336c1b22d7e859ebbc -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/morse-simulator/morse/find/40dcaf7c5ae79d72425c88a08339741aba5fab65" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref=""
    role="button" aria-label="Switch branches or tags" tabindex="0">
    <span class="octicon octicon-git-branch"></span>
    <i>tree:</i>
    <span class="js-select-button">40dcaf7c5a</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/blob/0.3_STABLE/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.3_STABLE"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.3_STABLE">0.3_STABLE</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/blob/0.4_STABLE/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.4_STABLE"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.4_STABLE">0.4_STABLE</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/blob/0.5_STABLE/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.5_STABLE"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.5_STABLE">0.5_STABLE</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/blob/0.6_STABLE/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.6_STABLE"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.6_STABLE">0.6_STABLE</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/blob/1.0_STABLE/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="1.0_STABLE"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.0_STABLE">1.0_STABLE</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/blob/1.1_STABLE/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="1.1_STABLE"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.1_STABLE">1.1_STABLE</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/blob/master/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/first_cmake_based_installation/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="first_cmake_based_installation"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="first_cmake_based_installation">first_cmake_based_installation</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/adapto_0.2.8/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="adapto_0.2.8"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="adapto_0.2.8">adapto_0.2.8</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/adapto_0.2.7/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="adapto_0.2.7"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="adapto_0.2.7">adapto_0.2.7</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/adapto_0.2.6/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="adapto_0.2.6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="adapto_0.2.6">adapto_0.2.6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/adapto_0.2.5/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="adapto_0.2.5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="adapto_0.2.5">adapto_0.2.5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/adapto_0.2.2/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="adapto_0.2.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="adapto_0.2.2">adapto_0.2.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/adapto_0.2.1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="adapto_0.2.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="adapto_0.2.1">adapto_0.2.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/adapto_0.2.0/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="adapto_0.2.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="adapto_0.2.0">adapto_0.2.0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/adapto_0.1.1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="adapto_0.1.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="adapto_0.1.1">adapto_0.1.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/adapto_0.1.0.0/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="adapto_0.1.0.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="adapto_0.1.0.0">adapto_0.1.0.0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/adapto_0.1.0/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="adapto_0.1.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="adapto_0.1.0">adapto_0.1.0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/1.1-beta2/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="1.1-beta2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.1-beta2">1.1-beta2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/1.1-beta1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="1.1-beta1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.1-beta1">1.1-beta1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/1.1-alpha1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="1.1-alpha1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.1-alpha1">1.1-alpha1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/1.1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="1.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.1">1.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/1.0-beta2/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="1.0-beta2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.0-beta2">1.0-beta2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/1.0-beta1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="1.0-beta1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.0-beta1">1.0-beta1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/1.0-alpha1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="1.0-alpha1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.0-alpha1">1.0-alpha1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/1.0.1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="1.0.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.0.1">1.0.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/1.0/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="1.0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="1.0">1.0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.6-beta1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.6-beta1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.6-beta1">0.6-beta1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.6-alpha/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.6-alpha"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.6-alpha">0.6-alpha</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.6/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.6"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.6">0.6</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.5-alpha/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.5-alpha"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.5-alpha">0.5-alpha</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.5a2/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.5a2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.5a2">0.5a2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.5.2/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.5.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.5.2">0.5.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.5.1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.5.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.5.1">0.5.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.5/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.5"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.5">0.5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.4.1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.4.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.4.1">0.4.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.4/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.4"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.4">0.4</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.3a2/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.3a2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.3a2">0.3a2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.3a1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.3a1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.3a1">0.3a1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.3/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.3"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.3">0.3</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.2b2/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.2b2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.2b2">0.2b2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.2b1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.2b1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.2b1">0.2b1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.2a1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.2a1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.2a1">0.2a1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.2a0/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.2a0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.2a0">0.2a0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.2.1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.2.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.2.1">0.2.1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.2/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.2">0.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.1alpha0/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.1alpha0"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.1alpha0">0.1alpha0</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.1a2/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.1a2"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.1a2">0.1a2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.1a1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.1a1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.1a1">0.1a1</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/morse-simulator/morse/tree/0.1/bindings/pymorse/src/pymorse/pymorse.py"
                 data-name="0.1"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="0.1">0.1</a>
            </div> <!-- /.select-menu-item -->
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/morse-simulator/morse/tree/40dcaf7c5ae79d72425c88a08339741aba5fab65" data-branch="40dcaf7c5ae79d72425c88a08339741aba5fab65" data-direction="back" data-pjax="true" itemscope="url" rel="nofollow"><span itemprop="title">morse</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/morse-simulator/morse/tree/40dcaf7c5ae79d72425c88a08339741aba5fab65/bindings" data-branch="40dcaf7c5ae79d72425c88a08339741aba5fab65" data-direction="back" data-pjax="true" itemscope="url" rel="nofollow"><span itemprop="title">bindings</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/morse-simulator/morse/tree/40dcaf7c5ae79d72425c88a08339741aba5fab65/bindings/pymorse" data-branch="40dcaf7c5ae79d72425c88a08339741aba5fab65" data-direction="back" data-pjax="true" itemscope="url" rel="nofollow"><span itemprop="title">pymorse</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/morse-simulator/morse/tree/40dcaf7c5ae79d72425c88a08339741aba5fab65/bindings/pymorse/src" data-branch="40dcaf7c5ae79d72425c88a08339741aba5fab65" data-direction="back" data-pjax="true" itemscope="url" rel="nofollow"><span itemprop="title">src</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/morse-simulator/morse/tree/40dcaf7c5ae79d72425c88a08339741aba5fab65/bindings/pymorse/src/pymorse" data-branch="40dcaf7c5ae79d72425c88a08339741aba5fab65" data-direction="back" data-pjax="true" itemscope="url" rel="nofollow"><span itemprop="title">pymorse</span></a></span><span class="separator"> / </span><strong class="final-path">pymorse.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="bindings/pymorse/src/pymorse/pymorse.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>



  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://1.gravatar.com/avatar/1337236386adb33b769026f2d98c3d29?d=https%3A%2F%2Fidenticons.github.com%2F867f291f08256ce4d77949b01c6a5508.png&amp;s=140" width="24" />
    <span class="author"><a href="/pierriko" rel="author">pierriko</a></span>
    <time class="js-relative-date" datetime="2013-06-07T03:17:11-07:00" title="2013-06-07 03:17:11">June 07, 2013</time>
    <div class="commit-title">
        <a href="/morse-simulator/morse/commit/a7f831fa1c87ddd9b641fbc479f5e58cfaa2d91f" class="message" data-pjax="true" title="[pymorse] readd suppressed last method for sensors">[pymorse] readd suppressed last method for sensors</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>4</strong> contributors</a></p>
          <a class="avatar tooltipped downwards" title="pierriko" href="/morse-simulator/morse/commits/40dcaf7c5ae79d72425c88a08339741aba5fab65/bindings/pymorse/src/pymorse/pymorse.py?author=pierriko"><img height="20" src="https://1.gravatar.com/avatar/1337236386adb33b769026f2d98c3d29?d=https%3A%2F%2Fidenticons.github.com%2F867f291f08256ce4d77949b01c6a5508.png&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="adegroote" href="/morse-simulator/morse/commits/40dcaf7c5ae79d72425c88a08339741aba5fab65/bindings/pymorse/src/pymorse/pymorse.py?author=adegroote"><img height="20" src="https://2.gravatar.com/avatar/0f37dd32246a8c59b5c0e933acb34128?d=https%3A%2F%2Fidenticons.github.com%2F5db57dc5ca10454fb07f4ea0075a9b77.png&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="severin-lemaignan" href="/morse-simulator/morse/commits/40dcaf7c5ae79d72425c88a08339741aba5fab65/bindings/pymorse/src/pymorse/pymorse.py?author=severin-lemaignan"><img height="20" src="https://0.gravatar.com/avatar/dee1aaed8a094315629ebf7883f58ec8?d=https%3A%2F%2Fidenticons.github.com%2Fd7c15011e74daa6ab354371ee44e7c09.png&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="lesire" href="/morse-simulator/morse/commits/40dcaf7c5ae79d72425c88a08339741aba5fab65/bindings/pymorse/src/pymorse/pymorse.py?author=lesire"><img height="20" src="https://2.gravatar.com/avatar/979500f2648d49d0e1451f257b638eb4?d=https%3A%2F%2Fidenticons.github.com%2Fe742a8f773d83d3ef9e2438e285e77b0.png&amp;s=140" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img height="24" src="https://1.gravatar.com/avatar/1337236386adb33b769026f2d98c3d29?d=https%3A%2F%2Fidenticons.github.com%2F867f291f08256ce4d77949b01c6a5508.png&amp;s=140" width="24" />
            <a href="/pierriko">pierriko</a>
          </li>
          <li class="facebox-user-list-item">
            <img height="24" src="https://2.gravatar.com/avatar/0f37dd32246a8c59b5c0e933acb34128?d=https%3A%2F%2Fidenticons.github.com%2F5db57dc5ca10454fb07f4ea0075a9b77.png&amp;s=140" width="24" />
            <a href="/adegroote">adegroote</a>
          </li>
          <li class="facebox-user-list-item">
            <img height="24" src="https://0.gravatar.com/avatar/dee1aaed8a094315629ebf7883f58ec8?d=https%3A%2F%2Fidenticons.github.com%2Fd7c15011e74daa6ab354371ee44e7c09.png&amp;s=140" width="24" />
            <a href="/severin-lemaignan">severin-lemaignan</a>
          </li>
          <li class="facebox-user-list-item">
            <img height="24" src="https://2.gravatar.com/avatar/979500f2648d49d0e1451f257b638eb4?d=https%3A%2F%2Fidenticons.github.com%2Fe742a8f773d83d3ef9e2438e285e77b0.png&amp;s=140" width="24" />
            <a href="/lesire">lesire</a>
          </li>
      </ul>
    </div>
  </div>

<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
          <span>783 lines (593 sloc)</span>
        <span>24.763 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton disabled js-entice" href=""
                 data-entice="You must be on a branch to make or propose changes to this file">Edit</a>
          <a href="/morse-simulator/morse/raw/40dcaf7c5ae79d72425c88a08339741aba5fab65/bindings/pymorse/src/pymorse/pymorse.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/morse-simulator/morse/blame/40dcaf7c5ae79d72425c88a08339741aba5fab65/bindings/pymorse/src/pymorse/pymorse.py" class="button minibutton ">Blame</a>
          <a href="/morse-simulator/morse/commits/40dcaf7c5ae79d72425c88a08339741aba5fab65/bindings/pymorse/src/pymorse/pymorse.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger empty-icon js-entice" href=""
             data-entice="You must be signed in and on a branch to make or propose changes">
          Delete
        </a>
      </div><!-- /.actions -->

    </div>
        <div class="blob-wrapper data type-python js-blob-data">
        <table class="file-code file-diff">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>
<span id="L424" rel="#L424">424</span>
<span id="L425" rel="#L425">425</span>
<span id="L426" rel="#L426">426</span>
<span id="L427" rel="#L427">427</span>
<span id="L428" rel="#L428">428</span>
<span id="L429" rel="#L429">429</span>
<span id="L430" rel="#L430">430</span>
<span id="L431" rel="#L431">431</span>
<span id="L432" rel="#L432">432</span>
<span id="L433" rel="#L433">433</span>
<span id="L434" rel="#L434">434</span>
<span id="L435" rel="#L435">435</span>
<span id="L436" rel="#L436">436</span>
<span id="L437" rel="#L437">437</span>
<span id="L438" rel="#L438">438</span>
<span id="L439" rel="#L439">439</span>
<span id="L440" rel="#L440">440</span>
<span id="L441" rel="#L441">441</span>
<span id="L442" rel="#L442">442</span>
<span id="L443" rel="#L443">443</span>
<span id="L444" rel="#L444">444</span>
<span id="L445" rel="#L445">445</span>
<span id="L446" rel="#L446">446</span>
<span id="L447" rel="#L447">447</span>
<span id="L448" rel="#L448">448</span>
<span id="L449" rel="#L449">449</span>
<span id="L450" rel="#L450">450</span>
<span id="L451" rel="#L451">451</span>
<span id="L452" rel="#L452">452</span>
<span id="L453" rel="#L453">453</span>
<span id="L454" rel="#L454">454</span>
<span id="L455" rel="#L455">455</span>
<span id="L456" rel="#L456">456</span>
<span id="L457" rel="#L457">457</span>
<span id="L458" rel="#L458">458</span>
<span id="L459" rel="#L459">459</span>
<span id="L460" rel="#L460">460</span>
<span id="L461" rel="#L461">461</span>
<span id="L462" rel="#L462">462</span>
<span id="L463" rel="#L463">463</span>
<span id="L464" rel="#L464">464</span>
<span id="L465" rel="#L465">465</span>
<span id="L466" rel="#L466">466</span>
<span id="L467" rel="#L467">467</span>
<span id="L468" rel="#L468">468</span>
<span id="L469" rel="#L469">469</span>
<span id="L470" rel="#L470">470</span>
<span id="L471" rel="#L471">471</span>
<span id="L472" rel="#L472">472</span>
<span id="L473" rel="#L473">473</span>
<span id="L474" rel="#L474">474</span>
<span id="L475" rel="#L475">475</span>
<span id="L476" rel="#L476">476</span>
<span id="L477" rel="#L477">477</span>
<span id="L478" rel="#L478">478</span>
<span id="L479" rel="#L479">479</span>
<span id="L480" rel="#L480">480</span>
<span id="L481" rel="#L481">481</span>
<span id="L482" rel="#L482">482</span>
<span id="L483" rel="#L483">483</span>
<span id="L484" rel="#L484">484</span>
<span id="L485" rel="#L485">485</span>
<span id="L486" rel="#L486">486</span>
<span id="L487" rel="#L487">487</span>
<span id="L488" rel="#L488">488</span>
<span id="L489" rel="#L489">489</span>
<span id="L490" rel="#L490">490</span>
<span id="L491" rel="#L491">491</span>
<span id="L492" rel="#L492">492</span>
<span id="L493" rel="#L493">493</span>
<span id="L494" rel="#L494">494</span>
<span id="L495" rel="#L495">495</span>
<span id="L496" rel="#L496">496</span>
<span id="L497" rel="#L497">497</span>
<span id="L498" rel="#L498">498</span>
<span id="L499" rel="#L499">499</span>
<span id="L500" rel="#L500">500</span>
<span id="L501" rel="#L501">501</span>
<span id="L502" rel="#L502">502</span>
<span id="L503" rel="#L503">503</span>
<span id="L504" rel="#L504">504</span>
<span id="L505" rel="#L505">505</span>
<span id="L506" rel="#L506">506</span>
<span id="L507" rel="#L507">507</span>
<span id="L508" rel="#L508">508</span>
<span id="L509" rel="#L509">509</span>
<span id="L510" rel="#L510">510</span>
<span id="L511" rel="#L511">511</span>
<span id="L512" rel="#L512">512</span>
<span id="L513" rel="#L513">513</span>
<span id="L514" rel="#L514">514</span>
<span id="L515" rel="#L515">515</span>
<span id="L516" rel="#L516">516</span>
<span id="L517" rel="#L517">517</span>
<span id="L518" rel="#L518">518</span>
<span id="L519" rel="#L519">519</span>
<span id="L520" rel="#L520">520</span>
<span id="L521" rel="#L521">521</span>
<span id="L522" rel="#L522">522</span>
<span id="L523" rel="#L523">523</span>
<span id="L524" rel="#L524">524</span>
<span id="L525" rel="#L525">525</span>
<span id="L526" rel="#L526">526</span>
<span id="L527" rel="#L527">527</span>
<span id="L528" rel="#L528">528</span>
<span id="L529" rel="#L529">529</span>
<span id="L530" rel="#L530">530</span>
<span id="L531" rel="#L531">531</span>
<span id="L532" rel="#L532">532</span>
<span id="L533" rel="#L533">533</span>
<span id="L534" rel="#L534">534</span>
<span id="L535" rel="#L535">535</span>
<span id="L536" rel="#L536">536</span>
<span id="L537" rel="#L537">537</span>
<span id="L538" rel="#L538">538</span>
<span id="L539" rel="#L539">539</span>
<span id="L540" rel="#L540">540</span>
<span id="L541" rel="#L541">541</span>
<span id="L542" rel="#L542">542</span>
<span id="L543" rel="#L543">543</span>
<span id="L544" rel="#L544">544</span>
<span id="L545" rel="#L545">545</span>
<span id="L546" rel="#L546">546</span>
<span id="L547" rel="#L547">547</span>
<span id="L548" rel="#L548">548</span>
<span id="L549" rel="#L549">549</span>
<span id="L550" rel="#L550">550</span>
<span id="L551" rel="#L551">551</span>
<span id="L552" rel="#L552">552</span>
<span id="L553" rel="#L553">553</span>
<span id="L554" rel="#L554">554</span>
<span id="L555" rel="#L555">555</span>
<span id="L556" rel="#L556">556</span>
<span id="L557" rel="#L557">557</span>
<span id="L558" rel="#L558">558</span>
<span id="L559" rel="#L559">559</span>
<span id="L560" rel="#L560">560</span>
<span id="L561" rel="#L561">561</span>
<span id="L562" rel="#L562">562</span>
<span id="L563" rel="#L563">563</span>
<span id="L564" rel="#L564">564</span>
<span id="L565" rel="#L565">565</span>
<span id="L566" rel="#L566">566</span>
<span id="L567" rel="#L567">567</span>
<span id="L568" rel="#L568">568</span>
<span id="L569" rel="#L569">569</span>
<span id="L570" rel="#L570">570</span>
<span id="L571" rel="#L571">571</span>
<span id="L572" rel="#L572">572</span>
<span id="L573" rel="#L573">573</span>
<span id="L574" rel="#L574">574</span>
<span id="L575" rel="#L575">575</span>
<span id="L576" rel="#L576">576</span>
<span id="L577" rel="#L577">577</span>
<span id="L578" rel="#L578">578</span>
<span id="L579" rel="#L579">579</span>
<span id="L580" rel="#L580">580</span>
<span id="L581" rel="#L581">581</span>
<span id="L582" rel="#L582">582</span>
<span id="L583" rel="#L583">583</span>
<span id="L584" rel="#L584">584</span>
<span id="L585" rel="#L585">585</span>
<span id="L586" rel="#L586">586</span>
<span id="L587" rel="#L587">587</span>
<span id="L588" rel="#L588">588</span>
<span id="L589" rel="#L589">589</span>
<span id="L590" rel="#L590">590</span>
<span id="L591" rel="#L591">591</span>
<span id="L592" rel="#L592">592</span>
<span id="L593" rel="#L593">593</span>
<span id="L594" rel="#L594">594</span>
<span id="L595" rel="#L595">595</span>
<span id="L596" rel="#L596">596</span>
<span id="L597" rel="#L597">597</span>
<span id="L598" rel="#L598">598</span>
<span id="L599" rel="#L599">599</span>
<span id="L600" rel="#L600">600</span>
<span id="L601" rel="#L601">601</span>
<span id="L602" rel="#L602">602</span>
<span id="L603" rel="#L603">603</span>
<span id="L604" rel="#L604">604</span>
<span id="L605" rel="#L605">605</span>
<span id="L606" rel="#L606">606</span>
<span id="L607" rel="#L607">607</span>
<span id="L608" rel="#L608">608</span>
<span id="L609" rel="#L609">609</span>
<span id="L610" rel="#L610">610</span>
<span id="L611" rel="#L611">611</span>
<span id="L612" rel="#L612">612</span>
<span id="L613" rel="#L613">613</span>
<span id="L614" rel="#L614">614</span>
<span id="L615" rel="#L615">615</span>
<span id="L616" rel="#L616">616</span>
<span id="L617" rel="#L617">617</span>
<span id="L618" rel="#L618">618</span>
<span id="L619" rel="#L619">619</span>
<span id="L620" rel="#L620">620</span>
<span id="L621" rel="#L621">621</span>
<span id="L622" rel="#L622">622</span>
<span id="L623" rel="#L623">623</span>
<span id="L624" rel="#L624">624</span>
<span id="L625" rel="#L625">625</span>
<span id="L626" rel="#L626">626</span>
<span id="L627" rel="#L627">627</span>
<span id="L628" rel="#L628">628</span>
<span id="L629" rel="#L629">629</span>
<span id="L630" rel="#L630">630</span>
<span id="L631" rel="#L631">631</span>
<span id="L632" rel="#L632">632</span>
<span id="L633" rel="#L633">633</span>
<span id="L634" rel="#L634">634</span>
<span id="L635" rel="#L635">635</span>
<span id="L636" rel="#L636">636</span>
<span id="L637" rel="#L637">637</span>
<span id="L638" rel="#L638">638</span>
<span id="L639" rel="#L639">639</span>
<span id="L640" rel="#L640">640</span>
<span id="L641" rel="#L641">641</span>
<span id="L642" rel="#L642">642</span>
<span id="L643" rel="#L643">643</span>
<span id="L644" rel="#L644">644</span>
<span id="L645" rel="#L645">645</span>
<span id="L646" rel="#L646">646</span>
<span id="L647" rel="#L647">647</span>
<span id="L648" rel="#L648">648</span>
<span id="L649" rel="#L649">649</span>
<span id="L650" rel="#L650">650</span>
<span id="L651" rel="#L651">651</span>
<span id="L652" rel="#L652">652</span>
<span id="L653" rel="#L653">653</span>
<span id="L654" rel="#L654">654</span>
<span id="L655" rel="#L655">655</span>
<span id="L656" rel="#L656">656</span>
<span id="L657" rel="#L657">657</span>
<span id="L658" rel="#L658">658</span>
<span id="L659" rel="#L659">659</span>
<span id="L660" rel="#L660">660</span>
<span id="L661" rel="#L661">661</span>
<span id="L662" rel="#L662">662</span>
<span id="L663" rel="#L663">663</span>
<span id="L664" rel="#L664">664</span>
<span id="L665" rel="#L665">665</span>
<span id="L666" rel="#L666">666</span>
<span id="L667" rel="#L667">667</span>
<span id="L668" rel="#L668">668</span>
<span id="L669" rel="#L669">669</span>
<span id="L670" rel="#L670">670</span>
<span id="L671" rel="#L671">671</span>
<span id="L672" rel="#L672">672</span>
<span id="L673" rel="#L673">673</span>
<span id="L674" rel="#L674">674</span>
<span id="L675" rel="#L675">675</span>
<span id="L676" rel="#L676">676</span>
<span id="L677" rel="#L677">677</span>
<span id="L678" rel="#L678">678</span>
<span id="L679" rel="#L679">679</span>
<span id="L680" rel="#L680">680</span>
<span id="L681" rel="#L681">681</span>
<span id="L682" rel="#L682">682</span>
<span id="L683" rel="#L683">683</span>
<span id="L684" rel="#L684">684</span>
<span id="L685" rel="#L685">685</span>
<span id="L686" rel="#L686">686</span>
<span id="L687" rel="#L687">687</span>
<span id="L688" rel="#L688">688</span>
<span id="L689" rel="#L689">689</span>
<span id="L690" rel="#L690">690</span>
<span id="L691" rel="#L691">691</span>
<span id="L692" rel="#L692">692</span>
<span id="L693" rel="#L693">693</span>
<span id="L694" rel="#L694">694</span>
<span id="L695" rel="#L695">695</span>
<span id="L696" rel="#L696">696</span>
<span id="L697" rel="#L697">697</span>
<span id="L698" rel="#L698">698</span>
<span id="L699" rel="#L699">699</span>
<span id="L700" rel="#L700">700</span>
<span id="L701" rel="#L701">701</span>
<span id="L702" rel="#L702">702</span>
<span id="L703" rel="#L703">703</span>
<span id="L704" rel="#L704">704</span>
<span id="L705" rel="#L705">705</span>
<span id="L706" rel="#L706">706</span>
<span id="L707" rel="#L707">707</span>
<span id="L708" rel="#L708">708</span>
<span id="L709" rel="#L709">709</span>
<span id="L710" rel="#L710">710</span>
<span id="L711" rel="#L711">711</span>
<span id="L712" rel="#L712">712</span>
<span id="L713" rel="#L713">713</span>
<span id="L714" rel="#L714">714</span>
<span id="L715" rel="#L715">715</span>
<span id="L716" rel="#L716">716</span>
<span id="L717" rel="#L717">717</span>
<span id="L718" rel="#L718">718</span>
<span id="L719" rel="#L719">719</span>
<span id="L720" rel="#L720">720</span>
<span id="L721" rel="#L721">721</span>
<span id="L722" rel="#L722">722</span>
<span id="L723" rel="#L723">723</span>
<span id="L724" rel="#L724">724</span>
<span id="L725" rel="#L725">725</span>
<span id="L726" rel="#L726">726</span>
<span id="L727" rel="#L727">727</span>
<span id="L728" rel="#L728">728</span>
<span id="L729" rel="#L729">729</span>
<span id="L730" rel="#L730">730</span>
<span id="L731" rel="#L731">731</span>
<span id="L732" rel="#L732">732</span>
<span id="L733" rel="#L733">733</span>
<span id="L734" rel="#L734">734</span>
<span id="L735" rel="#L735">735</span>
<span id="L736" rel="#L736">736</span>
<span id="L737" rel="#L737">737</span>
<span id="L738" rel="#L738">738</span>
<span id="L739" rel="#L739">739</span>
<span id="L740" rel="#L740">740</span>
<span id="L741" rel="#L741">741</span>
<span id="L742" rel="#L742">742</span>
<span id="L743" rel="#L743">743</span>
<span id="L744" rel="#L744">744</span>
<span id="L745" rel="#L745">745</span>
<span id="L746" rel="#L746">746</span>
<span id="L747" rel="#L747">747</span>
<span id="L748" rel="#L748">748</span>
<span id="L749" rel="#L749">749</span>
<span id="L750" rel="#L750">750</span>
<span id="L751" rel="#L751">751</span>
<span id="L752" rel="#L752">752</span>
<span id="L753" rel="#L753">753</span>
<span id="L754" rel="#L754">754</span>
<span id="L755" rel="#L755">755</span>
<span id="L756" rel="#L756">756</span>
<span id="L757" rel="#L757">757</span>
<span id="L758" rel="#L758">758</span>
<span id="L759" rel="#L759">759</span>
<span id="L760" rel="#L760">760</span>
<span id="L761" rel="#L761">761</span>
<span id="L762" rel="#L762">762</span>
<span id="L763" rel="#L763">763</span>
<span id="L764" rel="#L764">764</span>
<span id="L765" rel="#L765">765</span>
<span id="L766" rel="#L766">766</span>
<span id="L767" rel="#L767">767</span>
<span id="L768" rel="#L768">768</span>
<span id="L769" rel="#L769">769</span>
<span id="L770" rel="#L770">770</span>
<span id="L771" rel="#L771">771</span>
<span id="L772" rel="#L772">772</span>
<span id="L773" rel="#L773">773</span>
<span id="L774" rel="#L774">774</span>
<span id="L775" rel="#L775">775</span>
<span id="L776" rel="#L776">776</span>
<span id="L777" rel="#L777">777</span>
<span id="L778" rel="#L778">778</span>
<span id="L779" rel="#L779">779</span>
<span id="L780" rel="#L780">780</span>
<span id="L781" rel="#L781">781</span>
<span id="L782" rel="#L782">782</span>

            </td>
            <td class="blob-line-code">
                    <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python3</span></div><div class='line' id='LC2'><span class="sd">&quot;&quot;&quot;A Python interface to control `MORSE &lt;http://morse.openrobots.org&gt;`_,</span></div><div class='line' id='LC3'><span class="sd">*the robotics simulator*.</span></div><div class='line' id='LC4'><br/></div><div class='line' id='LC5'><span class="sd">The ``pymorse`` library exposes MORSE services and data stream with a</span></div><div class='line' id='LC6'><span class="sd">friendly Python API.</span></div><div class='line' id='LC7'><br/></div><div class='line' id='LC8'><span class="sd">It uses underneath the MORSE socket API.</span></div><div class='line' id='LC9'><br/></div><div class='line' id='LC10'><span class="sd">Usage</span></div><div class='line' id='LC11'><span class="sd">=====</span></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'><span class="sd">Creating a connection to the simulator</span></div><div class='line' id='LC14'><span class="sd">--------------------------------------</span></div><div class='line' id='LC15'><br/></div><div class='line' id='LC16'><span class="sd">- Import the ``pymorse`` module</span></div><div class='line' id='LC17'><span class="sd">- Create a context with the ``with`` statement:</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><span class="sd">.. code-block:: python</span></div><div class='line' id='LC20'><br/></div><div class='line' id='LC21'><span class="sd">    import pymorse</span></div><div class='line' id='LC22'><br/></div><div class='line' id='LC23'><span class="sd">    with pymorse.Morse() as simu:</span></div><div class='line' id='LC24'><span class="sd">        # ...</span></div><div class='line' id='LC25'><span class="sd">        pass</span></div><div class='line' id='LC26'><br/></div><div class='line' id='LC27'><br/></div><div class='line' id='LC28'><span class="sd">The context manager will take care of properly closing the connection to the</span></div><div class='line' id='LC29'><span class="sd">simulator.  You can also directly create an instance of the</span></div><div class='line' id='LC30'><span class="sd">:py:class:`pymorse.Morse` class, passing the host and/or port of the</span></div><div class='line' id='LC31'><span class="sd">simulator (defaults to localhost:4000). In this case, you must call</span></div><div class='line' id='LC32'><span class="sd">:py:meth:`pymorse.Morse.close` before leaving.</span></div><div class='line' id='LC33'><br/></div><div class='line' id='LC34'><span class="sd">- Once created, the context generates proxies for every robots in the scene,</span></div><div class='line' id='LC35'><span class="sd">  and every sensors and actuators for each robot.</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'><span class="sd">First example</span></div><div class='line' id='LC38'><span class="sd">-------------</span></div><div class='line' id='LC39'><br/></div><div class='line' id='LC40'><span class="sd">Let consider MORSE has been started with the following simulation script:</span></div><div class='line' id='LC41'><br/></div><div class='line' id='LC42'><span class="sd">.. code-block:: python</span></div><div class='line' id='LC43'><br/></div><div class='line' id='LC44'><span class="sd">    from morse.builder import *</span></div><div class='line' id='LC45'><br/></div><div class='line' id='LC46'><span class="sd">    # Add a robot with a position sensor and a motion controller</span></div><div class='line' id='LC47'><span class="sd">    r2d2 = ATRV()</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'><span class="sd">    pose = Pose()</span></div><div class='line' id='LC50'><span class="sd">    pose.add_interface(&#39;socket&#39;)</span></div><div class='line' id='LC51'><span class="sd">    r2d2.append(pose)</span></div><div class='line' id='LC52'><br/></div><div class='line' id='LC53'><span class="sd">    motion = Waypoint()</span></div><div class='line' id='LC54'><span class="sd">    motion.add_interface(&#39;socket&#39;)</span></div><div class='line' id='LC55'><span class="sd">    r2d2.append(motion)</span></div><div class='line' id='LC56'><br/></div><div class='line' id='LC57'><br/></div><div class='line' id='LC58'><span class="sd">    # Environment</span></div><div class='line' id='LC59'><span class="sd">    env = Environment(&#39;land-1/trees&#39;)</span></div><div class='line' id='LC60'><br/></div><div class='line' id='LC61'><span class="sd">The following Python program sends a destination to the robot, and prints in</span></div><div class='line' id='LC62'><span class="sd">background its pose:</span></div><div class='line' id='LC63'><br/></div><div class='line' id='LC64'><span class="sd">.. code-block:: python</span></div><div class='line' id='LC65'><br/></div><div class='line' id='LC66'><span class="sd">    import time</span></div><div class='line' id='LC67'><span class="sd">    import pymorse</span></div><div class='line' id='LC68'><br/></div><div class='line' id='LC69'><span class="sd">    def print_pos(pose):</span></div><div class='line' id='LC70'><span class="sd">        print(&quot;I&#39;m currently at %s&quot; % pose)</span></div><div class='line' id='LC71'><br/></div><div class='line' id='LC72'><span class="sd">    with pymorse.Morse() as simu:</span></div><div class='line' id='LC73'><br/></div><div class='line' id='LC74'><span class="sd">        # subscribes to updates from the Pose sensor by passing a callback</span></div><div class='line' id='LC75'><span class="sd">        simu.r2d2.pose.subscribe(print_pos)</span></div><div class='line' id='LC76'><br/></div><div class='line' id='LC77'><span class="sd">        # sends a destination</span></div><div class='line' id='LC78'><span class="sd">        simu.r2d2.motion.publish({&#39;x&#39; : 10.0, &#39;y&#39;: 5.0, &#39;z&#39;: 0.0,</span></div><div class='line' id='LC79'><span class="sd">                                  &#39;tolerance&#39; : 0.5,</span></div><div class='line' id='LC80'><span class="sd">                                  &#39;speed&#39; : 1.0})</span></div><div class='line' id='LC81'><br/></div><div class='line' id='LC82'><span class="sd">        # Leave a couple of millisec to the simulator to start the action</span></div><div class='line' id='LC83'><span class="sd">        time.sleep(0.1)</span></div><div class='line' id='LC84'><br/></div><div class='line' id='LC85'><span class="sd">        # waits until we reach the target</span></div><div class='line' id='LC86'><span class="sd">        while simu.r2d2.motion.get_status() != &quot;Arrived&quot;:</span></div><div class='line' id='LC87'><span class="sd">            time.sleep(0.5)</span></div><div class='line' id='LC88'><br/></div><div class='line' id='LC89'><span class="sd">        print(&quot;Here we are!&quot;)</span></div><div class='line' id='LC90'><br/></div><div class='line' id='LC91'><br/></div><div class='line' id='LC92'><span class="sd">Data stream manipulation</span></div><div class='line' id='LC93'><span class="sd">------------------------</span></div><div class='line' id='LC94'><br/></div><div class='line' id='LC95'><span class="sd">Every component (sensor or actuator) exposes a datastream interface,</span></div><div class='line' id='LC96'><span class="sd">either read-only (for sensors) or write-only (for actuators)</span></div><div class='line' id='LC97'><br/></div><div class='line' id='LC98'><span class="sd">They are accessible by their names, as defined in the simulation</span></div><div class='line' id='LC99'><span class="sd">script (cf example above).</span></div><div class='line' id='LC100'><br/></div><div class='line' id='LC101'><span class="sd">Streams are Python :py:class:`pymorse.Stream` objects. It offers several</span></div><div class='line' id='LC102'><span class="sd">methods to read data:</span></div><div class='line' id='LC103'><br/></div><div class='line' id='LC104'><span class="sd">- :py:meth:`pymorse.Stream.get`: blocks until new data are</span></div><div class='line' id='LC105'><span class="sd">  available and returns them.</span></div><div class='line' id='LC106'><span class="sd">- :py:meth:`pymorse.Stream.last`: returns the last/the n last (if</span></div><div class='line' id='LC107'><span class="sd">  an integer argument is passed) records received, or none/less, if</span></div><div class='line' id='LC108'><span class="sd">  none/less have been received.</span></div><div class='line' id='LC109'><span class="sd">- :py:meth:`pymorse.Stream.subscribe` (and</span></div><div class='line' id='LC110'><span class="sd">  :py:meth:`pymorse.Stream.unsubscribe`): this method is called</span></div><div class='line' id='LC111'><span class="sd">  with a callback that is triggered everytime incoming data is received.</span></div><div class='line' id='LC112'><br/></div><div class='line' id='LC113'><span class="sd">These methods are demonstrated in the example below:</span></div><div class='line' id='LC114'><br/></div><div class='line' id='LC115'><span class="sd">.. code-block:: python</span></div><div class='line' id='LC116'><br/></div><div class='line' id='LC117'><span class="sd">    import time</span></div><div class='line' id='LC118'><span class="sd">    import pymorse</span></div><div class='line' id='LC119'><br/></div><div class='line' id='LC120'><span class="sd">    def printer(data):</span></div><div class='line' id='LC121'><span class="sd">        print(&quot;Incoming data! &quot; + str(data))</span></div><div class='line' id='LC122'><br/></div><div class='line' id='LC123'><span class="sd">    with pymorse.Morse(&quot;localhost&quot;, 4000) as simu:</span></div><div class='line' id='LC124'><br/></div><div class='line' id='LC125'><span class="sd">        try:</span></div><div class='line' id='LC126'><span class="sd">            # Get the &#39;Pose&#39; sensor datastream</span></div><div class='line' id='LC127'><span class="sd">            pose = simu.r2d2.pose</span></div><div class='line' id='LC128'><br/></div><div class='line' id='LC129'><span class="sd">            # Blocks until something is available</span></div><div class='line' id='LC130'><span class="sd">            print(pose.get())</span></div><div class='line' id='LC131'><br/></div><div class='line' id='LC132'><span class="sd">            # Asynchronous read: the following line do not block.</span></div><div class='line' id='LC133'><span class="sd">            pose.subscribe(printer)</span></div><div class='line' id='LC134'><br/></div><div class='line' id='LC135'><span class="sd">            # Read for 10 sec</span></div><div class='line' id='LC136'><span class="sd">            time.sleep(10)</span></div><div class='line' id='LC137'><br/></div><div class='line' id='LC138'><span class="sd">        except pymorse.MorseServerError as mse:</span></div><div class='line' id='LC139'><span class="sd">            print(&#39;Oups! An error occured!&#39;)</span></div><div class='line' id='LC140'><span class="sd">            print(mse)</span></div><div class='line' id='LC141'><br/></div><div class='line' id='LC142'><span class="sd">Writing on actuator&#39;s datastreams is achieved with the</span></div><div class='line' id='LC143'><span class="sd">:py:meth:`pymorse.Stream.publish` method, as illustrated in the first example</span></div><div class='line' id='LC144'><span class="sd">above.</span></div><div class='line' id='LC145'><br/></div><div class='line' id='LC146'><span class="sd">The data format is always formatted as a JSON dictionary (which means that,</span></div><div class='line' id='LC147'><span class="sd">currently, binary data like images are not supported). The documentation page</span></div><div class='line' id='LC148'><span class="sd">of each component specify the exact content of the dictionary.</span></div><div class='line' id='LC149'><br/></div><div class='line' id='LC150'><span class="sd">Services</span></div><div class='line' id='LC151'><span class="sd">--------</span></div><div class='line' id='LC152'><br/></div><div class='line' id='LC153'><span class="sd">Some components export RPC services. Please refer to the components&#39;</span></div><div class='line' id='LC154'><span class="sd">documentation for details.</span></div><div class='line' id='LC155'><br/></div><div class='line' id='LC156'><span class="sd">These services can be accessed from `pymorse`, and mostly look like regular</span></div><div class='line' id='LC157'><span class="sd">methods:</span></div><div class='line' id='LC158'><br/></div><div class='line' id='LC159'><span class="sd">.. code-block:: python</span></div><div class='line' id='LC160'><br/></div><div class='line' id='LC161'><span class="sd">    import pymorse</span></div><div class='line' id='LC162'><br/></div><div class='line' id='LC163'><span class="sd">    with pymorse.Morse() as simu:</span></div><div class='line' id='LC164'><br/></div><div class='line' id='LC165'><span class="sd">        # Invokes the get_status service from the &#39;Waypoints&#39; actuator</span></div><div class='line' id='LC166'><span class="sd">        print(simu.r2d2.motion.get_status())</span></div><div class='line' id='LC167'><br/></div><div class='line' id='LC168'><span class="sd">However, these call are **asynchronous**: a call to</span></div><div class='line' id='LC169'><span class="sd">`simu.r2d2.motion.get_status()` does not block, and returns instead a</span></div><div class='line' id='LC170'><span class="sd">`future`. See the `concurrent.futures API</span></div><div class='line' id='LC171'><span class="sd">&lt;http://docs.python.org/dev/library/concurrent.futures.html&gt;`_ to learn more</span></div><div class='line' id='LC172'><span class="sd">about `futures`.</span></div><div class='line' id='LC173'><br/></div><div class='line' id='LC174'><span class="sd">Non-blocking call are useful for long lasting services, like in the example</span></div><div class='line' id='LC175'><span class="sd">below:</span></div><div class='line' id='LC176'><br/></div><div class='line' id='LC177'><span class="sd">.. code-block:: python</span></div><div class='line' id='LC178'><br/></div><div class='line' id='LC179'><span class="sd">    import time</span></div><div class='line' id='LC180'><span class="sd">    import pymorse</span></div><div class='line' id='LC181'><br/></div><div class='line' id='LC182'><span class="sd">    def done(evt):</span></div><div class='line' id='LC183'><span class="sd">        print(&quot;We have reached our destination!&quot;)</span></div><div class='line' id='LC184'><br/></div><div class='line' id='LC185'><span class="sd">    with pymorse.Morse() as simu:</span></div><div class='line' id='LC186'><br/></div><div class='line' id='LC187'><span class="sd">        # Start the motion. It may take several seconds before finishing</span></div><div class='line' id='LC188'><span class="sd">        # The line below is however non-blocking</span></div><div class='line' id='LC189'><span class="sd">        goto_action = simu.r2d2.motion.goto(2.5, 0, 0)</span></div><div class='line' id='LC190'><br/></div><div class='line' id='LC191'><span class="sd">        # Register a callback to know when the action is done</span></div><div class='line' id='LC192'><span class="sd">        goto_action.add_done_callback(done)</span></div><div class='line' id='LC193'><br/></div><div class='line' id='LC194'><span class="sd">        print(&quot;Am I currently moving? %s&quot; % goto_action.running())</span></div><div class='line' id='LC195'><br/></div><div class='line' id='LC196'><span class="sd">        while goto_action.running():</span></div><div class='line' id='LC197'><span class="sd">            time.sleep(0.5)</span></div><div class='line' id='LC198'><br/></div><div class='line' id='LC199'><span class="sd">Use the `cancel` method on the `future` returned by the RPC call to</span></div><div class='line' id='LC200'><span class="sd">abort the service.</span></div><div class='line' id='LC201'><br/></div><div class='line' id='LC202'><span class="sd">To actually wait for a result, call the `result` method on the future:</span></div><div class='line' id='LC203'><br/></div><div class='line' id='LC204'><span class="sd">.. code-block:: python</span></div><div class='line' id='LC205'><br/></div><div class='line' id='LC206'><span class="sd">    import pymorse</span></div><div class='line' id='LC207'><br/></div><div class='line' id='LC208'><span class="sd">    with pymorse.Morse() as simu:</span></div><div class='line' id='LC209'><br/></div><div class='line' id='LC210'><span class="sd">        status = simu.r2d2.motion.get_status().result()</span></div><div class='line' id='LC211'><br/></div><div class='line' id='LC212'><span class="sd">        if status == &quot;Arrived&quot;:</span></div><div class='line' id='LC213'><span class="sd">            print(&quot;Here we are&quot;)</span></div><div class='line' id='LC214'><br/></div><div class='line' id='LC215'><span class="sd">However, for certain common cases (printing or comparing the return value), the</span></div><div class='line' id='LC216'><span class="sd">`result()` method is automatically called. Thus, the previous code sample can</span></div><div class='line' id='LC217'><span class="sd">be rewritten:</span></div><div class='line' id='LC218'><br/></div><div class='line' id='LC219'><span class="sd">.. code-block:: python</span></div><div class='line' id='LC220'><br/></div><div class='line' id='LC221'><span class="sd">    import pymorse</span></div><div class='line' id='LC222'><br/></div><div class='line' id='LC223'><span class="sd">    with pymorse.Morse() as simu:</span></div><div class='line' id='LC224'><br/></div><div class='line' id='LC225'><span class="sd">        if simu.r2d2.motion.get_status() == &quot;Arrived&quot;:</span></div><div class='line' id='LC226'><span class="sd">            print(&quot;Here we are&quot;)</span></div><div class='line' id='LC227'><br/></div><div class='line' id='LC228'><br/></div><div class='line' id='LC229'><span class="sd">Simulator control</span></div><div class='line' id='LC230'><span class="sd">-----------------</span></div><div class='line' id='LC231'><br/></div><div class='line' id='LC232'><span class="sd">Several services are available to control the overall behaviour of the</span></div><div class='line' id='LC233'><span class="sd">simulator.</span></div><div class='line' id='LC234'><br/></div><div class='line' id='LC235'><span class="sd">The whole list of such services is here: `Supervision services</span></div><div class='line' id='LC236'><span class="sd">&lt;http://www.openrobots.org/morse/doc/latest/user/supervision_services.html&gt;`_.</span></div><div class='line' id='LC237'><br/></div><div class='line' id='LC238'><span class="sd">For instance, you can stop the simulator (MORSE will quit) with</span></div><div class='line' id='LC239'><span class="sd">:py:meth:`pymorse.quit`, and reset it with :py:meth:`pymorse.Morse.reset`.</span></div><div class='line' id='LC240'><br/></div><div class='line' id='LC241'><span class="sd">These methods are demonstrated in the example below:</span></div><div class='line' id='LC242'><br/></div><div class='line' id='LC243'><span class="sd">.. code-block:: python</span></div><div class='line' id='LC244'><br/></div><div class='line' id='LC245'><span class="sd">    import pymorse</span></div><div class='line' id='LC246'><br/></div><div class='line' id='LC247'><span class="sd">    with pymorse.Morse(&quot;localhost&quot;, 4000) as simu:</span></div><div class='line' id='LC248'><br/></div><div class='line' id='LC249'><span class="sd">        try:</span></div><div class='line' id='LC250'><span class="sd">            print(simu.robots)</span></div><div class='line' id='LC251'><span class="sd">            simu.quit()</span></div><div class='line' id='LC252'><br/></div><div class='line' id='LC253'><span class="sd">        except pymorse.MorseServerError as mse:</span></div><div class='line' id='LC254'><span class="sd">            print(&#39;Oups! An error occured!&#39;)</span></div><div class='line' id='LC255'><span class="sd">            print(mse)</span></div><div class='line' id='LC256'><br/></div><div class='line' id='LC257'><span class="sd">Logging</span></div><div class='line' id='LC258'><span class="sd">=======</span></div><div class='line' id='LC259'><br/></div><div class='line' id='LC260'><span class="sd">This library use the standard Python logging mechanism.  You can</span></div><div class='line' id='LC261'><span class="sd">retrieve pymorse log messages through the &quot;pymorse&quot; logger.</span></div><div class='line' id='LC262'><br/></div><div class='line' id='LC263'><span class="sd">The complete example below shows how to retrieve the logger and how to</span></div><div class='line' id='LC264'><span class="sd">configure it to print debug messages on the console.</span></div><div class='line' id='LC265'><br/></div><div class='line' id='LC266'><span class="sd">.. code-block:: python</span></div><div class='line' id='LC267'><br/></div><div class='line' id='LC268'><span class="sd">    import logging</span></div><div class='line' id='LC269'><span class="sd">    import pymorse</span></div><div class='line' id='LC270'><br/></div><div class='line' id='LC271'><span class="sd">    logger = logging.getLogger(&quot;pymorse&quot;)</span></div><div class='line' id='LC272'><br/></div><div class='line' id='LC273'><span class="sd">    console = logging.StreamHandler()</span></div><div class='line' id='LC274'><span class="sd">    console.setLevel(logging.DEBUG)</span></div><div class='line' id='LC275'><span class="sd">    formatter = logging.Formatter(&#39;%(asctime)-15s %(name)s: %(levelname)s - %(message)s&#39;)</span></div><div class='line' id='LC276'><span class="sd">    console.setFormatter(formatter)</span></div><div class='line' id='LC277'><br/></div><div class='line' id='LC278'><span class="sd">    logger.addHandler(console)</span></div><div class='line' id='LC279'><br/></div><div class='line' id='LC280'><span class="sd">    with pymorse.Morse(&quot;localhost&quot;, 4000) as simu:</span></div><div class='line' id='LC281'><br/></div><div class='line' id='LC282'><span class="sd">        try:</span></div><div class='line' id='LC283'><span class="sd">            print(simu.robots)</span></div><div class='line' id='LC284'><br/></div><div class='line' id='LC285'><span class="sd">            simu.quit()</span></div><div class='line' id='LC286'><br/></div><div class='line' id='LC287'><span class="sd">        except pymorse.MorseServerError as mse:</span></div><div class='line' id='LC288'><span class="sd">            print(&#39;Oups! An error occured!&#39;)</span></div><div class='line' id='LC289'><span class="sd">            print(mse)</span></div><div class='line' id='LC290'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC291'><span class="kn">import</span> <span class="nn">json</span></div><div class='line' id='LC292'><span class="kn">import</span> <span class="nn">time</span></div><div class='line' id='LC293'><span class="kn">import</span> <span class="nn">socket</span></div><div class='line' id='LC294'><span class="kn">import</span> <span class="nn">logging</span></div><div class='line' id='LC295'><span class="kn">import</span> <span class="nn">asyncore</span></div><div class='line' id='LC296'><span class="kn">import</span> <span class="nn">asynchat</span></div><div class='line' id='LC297'><span class="kn">import</span> <span class="nn">threading</span></div><div class='line' id='LC298'><span class="c"># Double-ended queue, thread-safe append/pop.</span></div><div class='line' id='LC299'><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">deque</span></div><div class='line' id='LC300'><br/></div><div class='line' id='LC301'><span class="kn">from</span> <span class="nn">.future</span> <span class="kn">import</span> <span class="n">MorseExecutor</span></div><div class='line' id='LC302'><br/></div><div class='line' id='LC303'><span class="n">logger</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">(</span><span class="s">&quot;pymorse&quot;</span><span class="p">)</span></div><div class='line' id='LC304'><span class="n">logger</span><span class="o">.</span><span class="n">setLevel</span><span class="p">(</span><span class="n">logging</span><span class="o">.</span><span class="n">WARNING</span><span class="p">)</span></div><div class='line' id='LC305'><span class="c"># logger.addHandler( logging.NullHandler() )</span></div><div class='line' id='LC306'><br/></div><div class='line' id='LC307'><span class="n">MSG_SEPARATOR</span><span class="o">=</span><span class="n">b</span><span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span></div><div class='line' id='LC308'><span class="n">TIMEOUT</span><span class="o">=</span><span class="mi">8</span></div><div class='line' id='LC309'><span class="n">BUFFER_SIZE</span><span class="o">=</span><span class="mi">8192</span></div><div class='line' id='LC310'><span class="n">SUCCESS</span><span class="o">=</span><span class="s">&#39;SUCCESS&#39;</span></div><div class='line' id='LC311'><span class="n">FAILURE</span><span class="o">=</span><span class="s">&#39;FAILED&#39;</span></div><div class='line' id='LC312'><span class="n">PREEMPTED</span><span class="o">=</span><span class="s">&#39;PREEMPTED&#39;</span></div><div class='line' id='LC313'><br/></div><div class='line' id='LC314'><span class="k">class</span> <span class="nc">MorseServiceError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span></div><div class='line' id='LC315'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; Morse Service Exception thrown when unknown error &quot;&quot;&quot;</span></div><div class='line' id='LC316'><br/></div><div class='line' id='LC317'><span class="k">class</span> <span class="nc">MorseServiceFailed</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span></div><div class='line' id='LC318'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; Morse Service Exception thrown when failed error &quot;&quot;&quot;</span></div><div class='line' id='LC319'><br/></div><div class='line' id='LC320'><span class="k">class</span> <span class="nc">MorseServicePreempted</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span></div><div class='line' id='LC321'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; Morse Service Exception thrown when preempted error &quot;&quot;&quot;</span></div><div class='line' id='LC322'><br/></div><div class='line' id='LC323'><br/></div><div class='line' id='LC324'><span class="k">class</span> <span class="nc">Component</span><span class="p">():</span></div><div class='line' id='LC325'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">morse</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">fqn</span><span class="p">,</span> <span class="n">stream</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span> <span class="n">port</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span> <span class="n">services</span> <span class="o">=</span> <span class="p">[]):</span></div><div class='line' id='LC326'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_morse</span> <span class="o">=</span> <span class="n">morse</span></div><div class='line' id='LC327'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span></div><div class='line' id='LC328'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">fqn</span> <span class="o">=</span> <span class="n">fqn</span> <span class="c"># fully qualified name</span></div><div class='line' id='LC329'><br/></div><div class='line' id='LC330'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">port</span><span class="p">:</span></div><div class='line' id='LC331'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">stream</span> <span class="o">=</span> <span class="n">StreamJSON</span><span class="p">(</span><span class="n">morse</span><span class="o">.</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span></div><div class='line' id='LC332'><br/></div><div class='line' id='LC333'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">stream</span> <span class="o">==</span> <span class="s">&#39;IN&#39;</span><span class="p">:</span></div><div class='line' id='LC334'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">publish</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream</span><span class="o">.</span><span class="n">publish</span></div><div class='line' id='LC335'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">stream</span> <span class="o">==</span> <span class="s">&#39;OUT&#39;</span><span class="p">:</span></div><div class='line' id='LC336'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">get</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream</span><span class="o">.</span><span class="n">get</span></div><div class='line' id='LC337'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream</span><span class="o">.</span><span class="n">last</span></div><div class='line' id='LC338'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">subscribe</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream</span><span class="o">.</span><span class="n">subscribe</span></div><div class='line' id='LC339'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">unsubscribe</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream</span><span class="o">.</span><span class="n">unsubscribe</span></div><div class='line' id='LC340'><br/></div><div class='line' id='LC341'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">service</span> <span class="ow">in</span> <span class="n">services</span><span class="p">:</span></div><div class='line' id='LC342'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&quot;Adding service </span><span class="si">%s</span><span class="s"> to component </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">service</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">))</span></div><div class='line' id='LC343'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_add_service</span><span class="p">(</span><span class="n">service</span><span class="p">)</span></div><div class='line' id='LC344'><br/></div><div class='line' id='LC345'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_add_service</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="p">):</span></div><div class='line' id='LC346'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">innermethod</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">):</span></div><div class='line' id='LC347'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&quot;Sending asynchronous request </span><span class="si">%s</span><span class="s"> with args </span><span class="si">%s</span><span class="s">.&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">method</span><span class="p">,</span> <span class="n">args</span><span class="p">))</span></div><div class='line' id='LC348'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">req</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_morse</span><span class="o">.</span><span class="n">_rpc_request</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fqn</span><span class="p">,</span> <span class="n">method</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span></div><div class='line' id='LC349'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">future</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_morse</span><span class="o">.</span><span class="n">executor</span><span class="o">.</span><span class="n">submit</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_morse</span><span class="o">.</span><span class="n">_rpc_process</span><span class="p">,</span> <span class="n">req</span><span class="p">)</span></div><div class='line' id='LC350'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#TODO: find a way to throw an execption in the main thread</span></div><div class='line' id='LC351'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># if the RPC request fails at invokation for stupid reasons</span></div><div class='line' id='LC352'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># like wrong # of params</span></div><div class='line' id='LC353'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">future</span></div><div class='line' id='LC354'><br/></div><div class='line' id='LC355'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">innermethod</span><span class="o">.</span><span class="n">__doc__</span> <span class="o">=</span> <span class="s">&quot;This method is a proxy for the MORSE </span><span class="si">%s</span><span class="s"> service.&quot;</span> <span class="o">%</span> <span class="n">method</span></div><div class='line' id='LC356'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">innermethod</span><span class="o">.</span><span class="n">__name__</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">method</span><span class="p">)</span></div><div class='line' id='LC357'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">setattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">innermethod</span><span class="o">.</span><span class="n">__name__</span><span class="p">,</span> <span class="n">innermethod</span><span class="p">)</span></div><div class='line' id='LC358'><br/></div><div class='line' id='LC359'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">close</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC360'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream</span><span class="p">:</span></div><div class='line' id='LC361'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">stream</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC362'><br/></div><div class='line' id='LC363'><span class="k">class</span> <span class="nc">Robot</span><span class="p">(</span><span class="nb">dict</span><span class="p">,</span> <span class="n">Component</span><span class="p">):</span></div><div class='line' id='LC364'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">__getattr__</span> <span class="o">=</span> <span class="nb">dict</span><span class="o">.</span><span class="n">__getitem__</span></div><div class='line' id='LC365'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">__setattr__</span> <span class="o">=</span> <span class="nb">dict</span><span class="o">.</span><span class="n">__setitem__</span></div><div class='line' id='LC366'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">__delattr__</span> <span class="o">=</span> <span class="nb">dict</span><span class="o">.</span><span class="n">__delitem__</span></div><div class='line' id='LC367'><br/></div><div class='line' id='LC368'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">morse</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">fqn</span><span class="p">,</span> <span class="n">services</span> <span class="o">=</span> <span class="p">[]):</span></div><div class='line' id='LC369'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Component</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">morse</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">fqn</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="n">services</span><span class="p">)</span></div><div class='line' id='LC370'><br/></div><div class='line' id='LC371'><span class="k">def</span> <span class="nf">normalize_name</span><span class="p">(</span><span class="n">name</span><span class="p">):</span></div><div class='line' id='LC372'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Normalize Blender names to get valid Python identifiers&quot;&quot;&quot;</span></div><div class='line' id='LC373'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">normalized</span> <span class="o">=</span> <span class="n">name</span></div><div class='line' id='LC374'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">illegal</span> <span class="ow">in</span> <span class="s">&quot;.-~&quot;</span><span class="p">:</span></div><div class='line' id='LC375'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">normalized</span> <span class="o">=</span> <span class="n">normalized</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">illegal</span><span class="p">,</span> <span class="s">&quot;_&quot;</span><span class="p">)</span></div><div class='line' id='LC376'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">normalized</span></div><div class='line' id='LC377'><br/></div><div class='line' id='LC378'><span class="k">def</span> <span class="nf">parse_response</span><span class="p">(</span><span class="n">raw</span><span class="p">):</span></div><div class='line' id='LC379'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC380'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC381'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">msg_id</span><span class="p">,</span> <span class="n">status</span><span class="p">,</span> <span class="n">result</span> <span class="o">=</span> <span class="n">raw</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span></div><div class='line' id='LC382'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC383'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">result</span><span class="p">)</span></div><div class='line' id='LC384'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">TypeError</span><span class="p">:</span></div><div class='line' id='LC385'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&quot;Could not deserialize MORSE answer! Got: &lt;</span><span class="si">%s</span><span class="s">&gt;&quot;</span> <span class="o">%</span> <span class="n">result</span><span class="p">)</span></div><div class='line' id='LC386'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span></div><div class='line' id='LC387'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># No return value</span></div><div class='line' id='LC388'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39; &#39;</span> <span class="ow">in</span> <span class="n">raw</span><span class="p">:</span></div><div class='line' id='LC389'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">msg_id</span><span class="p">,</span> <span class="n">status</span> <span class="o">=</span> <span class="n">raw</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">)</span></div><div class='line' id='LC390'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC391'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s">&quot;Could not receive a valid response from MORSE: &lt;</span><span class="si">%s</span><span class="s">&gt;&quot;</span> <span class="o">%</span> <span class="n">raw</span><span class="p">)</span></div><div class='line' id='LC392'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">msg_id</span> <span class="o">=</span> <span class="s">&#39;???&#39;</span></div><div class='line' id='LC393'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">status</span> <span class="o">=</span> <span class="n">FAILURE</span></div><div class='line' id='LC394'><br/></div><div class='line' id='LC395'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&quot;Got answer: </span><span class="si">%s</span><span class="s">, </span><span class="si">%s</span><span class="s">&quot;</span><span class="o">%</span><span class="p">(</span><span class="n">status</span><span class="p">,</span> <span class="n">result</span><span class="p">))</span></div><div class='line' id='LC396'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">{</span></div><div class='line' id='LC397'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;id&quot;</span><span class="p">:</span> <span class="n">msg_id</span><span class="p">,</span></div><div class='line' id='LC398'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;status&quot;</span><span class="p">:</span> <span class="n">status</span><span class="p">,</span></div><div class='line' id='LC399'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;result&quot;</span><span class="p">:</span> <span class="n">result</span><span class="p">,</span></div><div class='line' id='LC400'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC401'><br/></div><div class='line' id='LC402'><span class="k">def</span> <span class="nf">rpc_get_result</span><span class="p">(</span><span class="n">response</span><span class="p">):</span></div><div class='line' id='LC403'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s">&#39;result&#39;</span><span class="p">]</span></div><div class='line' id='LC404'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">status</span> <span class="o">=</span> <span class="n">response</span><span class="p">[</span><span class="s">&#39;status&#39;</span><span class="p">]</span></div><div class='line' id='LC405'><br/></div><div class='line' id='LC406'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">status</span> <span class="o">==</span> <span class="n">SUCCESS</span><span class="p">:</span></div><div class='line' id='LC407'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">result</span></div><div class='line' id='LC408'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">status</span> <span class="o">==</span> <span class="n">FAILURE</span><span class="p">:</span></div><div class='line' id='LC409'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">result</span> <span class="ow">and</span> <span class="s">&quot;wrong # of parameters&quot;</span> <span class="ow">in</span> <span class="n">result</span><span class="p">:</span></div><div class='line' id='LC410'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="n">result</span><span class="p">)</span></div><div class='line' id='LC411'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">MorseServiceFailed</span><span class="p">(</span><span class="n">result</span><span class="p">)</span></div><div class='line' id='LC412'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">status</span> <span class="o">==</span> <span class="n">PREEMPTED</span><span class="p">:</span></div><div class='line' id='LC413'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">MorseServicePreempted</span><span class="p">(</span><span class="n">result</span><span class="p">)</span></div><div class='line' id='LC414'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC415'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">MorseServiceError</span><span class="p">(</span><span class="n">result</span><span class="p">)</span></div><div class='line' id='LC416'><br/></div><div class='line' id='LC417'><span class="k">class</span> <span class="nc">ResponseCallback</span><span class="p">:</span></div><div class='line' id='LC418'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">_conditions</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC419'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">req_id</span><span class="p">):</span></div><div class='line' id='LC420'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">request_id</span> <span class="o">=</span> <span class="n">req_id</span></div><div class='line' id='LC421'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">response</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC422'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">condition</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">Condition</span><span class="p">()</span></div><div class='line' id='LC423'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ResponseCallback</span><span class="o">.</span><span class="n">_conditions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">condition</span><span class="p">)</span></div><div class='line' id='LC424'><br/></div><div class='line' id='LC425'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">callback</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">res_bytes</span><span class="p">):</span></div><div class='line' id='LC426'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="n">parse_response</span><span class="p">(</span><span class="n">res_bytes</span><span class="p">)</span></div><div class='line' id='LC427'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">response</span><span class="p">[</span><span class="s">&#39;id&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">request_id</span><span class="p">:</span></div><div class='line' id='LC428'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">response</span> <span class="o">=</span> <span class="n">response</span></div><div class='line' id='LC429'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">condition</span><span class="p">:</span></div><div class='line' id='LC430'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ResponseCallback</span><span class="o">.</span><span class="n">_conditions</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">condition</span><span class="p">)</span></div><div class='line' id='LC431'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">condition</span><span class="o">.</span><span class="n">notify_all</span><span class="p">()</span></div><div class='line' id='LC432'><br/></div><div class='line' id='LC433'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">cancel_all</span><span class="p">():</span></div><div class='line' id='LC434'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">condition</span> <span class="ow">in</span> <span class="n">ResponseCallback</span><span class="o">.</span><span class="n">_conditions</span><span class="p">:</span></div><div class='line' id='LC435'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">with</span> <span class="n">condition</span><span class="p">:</span></div><div class='line' id='LC436'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">condition</span><span class="o">.</span><span class="n">notify_all</span><span class="p">()</span></div><div class='line' id='LC437'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">del</span> <span class="n">ResponseCallback</span><span class="o">.</span><span class="n">_conditions</span><span class="p">[:]</span> <span class="c"># clear list</span></div><div class='line' id='LC438'><br/></div><div class='line' id='LC439'><br/></div><div class='line' id='LC440'><span class="k">class</span> <span class="nc">Morse</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC441'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">_asyncore_thread</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC442'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span> <span class="o">=</span> <span class="s">&quot;localhost&quot;</span><span class="p">,</span> <span class="n">port</span> <span class="o">=</span> <span class="mi">4000</span><span class="p">):</span></div><div class='line' id='LC443'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; Creates an instance of the MORSE simulator proxy.</span></div><div class='line' id='LC444'><br/></div><div class='line' id='LC445'><span class="sd">        This is the main object you need to instanciate to communicate with the simulator.</span></div><div class='line' id='LC446'><br/></div><div class='line' id='LC447'><span class="sd">        :param host: the simulator host (default: localhost)</span></div><div class='line' id='LC448'><span class="sd">        :param port: the port of the simulator socket interface (default: 4000)</span></div><div class='line' id='LC449'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC450'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">host</span> <span class="o">=</span> <span class="n">host</span></div><div class='line' id='LC451'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">simulator_service</span> <span class="o">=</span> <span class="n">Stream</span><span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span></div><div class='line' id='LC452'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">simulator_service_id</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC453'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">Morse</span><span class="o">.</span><span class="n">_asyncore_thread</span><span class="p">:</span></div><div class='line' id='LC454'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Morse</span><span class="o">.</span><span class="n">_asyncore_thread</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="p">(</span> <span class="n">target</span> <span class="o">=</span> <span class="n">asyncore</span><span class="o">.</span><span class="n">loop</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;timeout&#39;</span><span class="p">:</span> <span class="mf">0.01</span><span class="p">}</span> <span class="p">)</span></div><div class='line' id='LC455'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Morse</span><span class="o">.</span><span class="n">_asyncore_thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span></div><div class='line' id='LC456'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&quot;Morse thread started&quot;</span><span class="p">)</span></div><div class='line' id='LC457'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC458'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&quot;Morse thread was already started&quot;</span><span class="p">)</span></div><div class='line' id='LC459'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">executor</span> <span class="o">=</span> <span class="n">MorseExecutor</span><span class="p">(</span><span class="n">max_workers</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span> <span class="n">morse</span> <span class="o">=</span> <span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC460'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">initialize_api</span><span class="p">()</span></div><div class='line' id='LC461'><br/></div><div class='line' id='LC462'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">is_up</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC463'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">simulator_service</span><span class="o">.</span><span class="n">is_up</span><span class="p">()</span></div><div class='line' id='LC464'><br/></div><div class='line' id='LC465'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">initialize_api</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC466'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; This method asks MORSE for the scene structure, and</span></div><div class='line' id='LC467'><span class="sd">        dynamically creates corresponding objects in &#39;self&#39;.</span></div><div class='line' id='LC468'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC469'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">details</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rpc_t</span><span class="p">(</span><span class="mi">15</span><span class="p">,</span> <span class="s">&#39;simulation&#39;</span><span class="p">,</span> <span class="s">&#39;details&#39;</span><span class="p">)</span> <span class="c"># RPC with timeout</span></div><div class='line' id='LC470'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">details</span><span class="p">:</span></div><div class='line' id='LC471'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;simulation details not available&quot;</span><span class="p">)</span></div><div class='line' id='LC472'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="n">details</span><span class="p">)</span></div><div class='line' id='LC473'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">robots</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC474'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">robot_detail</span> <span class="ow">in</span> <span class="n">details</span><span class="p">[</span><span class="s">&quot;robots&quot;</span><span class="p">]:</span></div><div class='line' id='LC475'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span> <span class="o">=</span> <span class="n">normalize_name</span><span class="p">(</span><span class="n">robot_detail</span><span class="p">[</span><span class="s">&quot;name&quot;</span><span class="p">])</span></div><div class='line' id='LC476'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">robots</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">name</span><span class="p">)</span></div><div class='line' id='LC477'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">robot</span> <span class="o">=</span> <span class="n">Robot</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">robot_detail</span><span class="p">[</span><span class="s">&#39;name&#39;</span><span class="p">],</span> <span class="n">robot_detail</span><span class="p">[</span><span class="s">&#39;name&#39;</span><span class="p">],</span></div><div class='line' id='LC478'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">services</span> <span class="o">=</span> <span class="n">robot_detail</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;services&#39;</span><span class="p">,</span> <span class="p">[]))</span></div><div class='line' id='LC479'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">setattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">robot</span><span class="p">)</span></div><div class='line' id='LC480'><br/></div><div class='line' id='LC481'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">components</span> <span class="o">=</span> <span class="n">robot_detail</span><span class="p">[</span><span class="s">&quot;components&quot;</span><span class="p">]</span></div><div class='line' id='LC482'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># important to sort the list of components to ensure parents are</span></div><div class='line' id='LC483'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># created before children</span></div><div class='line' id='LC484'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">component</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">components</span><span class="o">.</span><span class="n">keys</span><span class="p">()):</span></div><div class='line' id='LC485'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_add_component</span><span class="p">(</span><span class="n">robot</span><span class="p">,</span> <span class="n">component</span><span class="p">,</span> <span class="n">components</span><span class="p">[</span><span class="n">component</span><span class="p">])</span></div><div class='line' id='LC486'><br/></div><div class='line' id='LC487'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_add_component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">robot</span><span class="p">,</span> <span class="n">fqn</span><span class="p">,</span> <span class="n">details</span><span class="p">):</span></div><div class='line' id='LC488'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stream</span> <span class="o">=</span> <span class="n">details</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;stream&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></div><div class='line' id='LC489'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">port</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC490'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">stream</span><span class="p">:</span></div><div class='line' id='LC491'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC492'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">port</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_stream_port</span><span class="p">(</span><span class="n">fqn</span><span class="p">)</span></div><div class='line' id='LC493'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="n">MorseServiceFailed</span><span class="p">:</span></div><div class='line' id='LC494'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s">&#39;Component &lt;</span><span class="si">%s</span><span class="s">&gt; has a non-socket stream: datastream via pymorse not supported&#39;</span><span class="p">,</span> <span class="n">fqn</span><span class="p">)</span></div><div class='line' id='LC495'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stream</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC496'><br/></div><div class='line' id='LC497'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">services</span> <span class="o">=</span> <span class="n">details</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;services&#39;</span><span class="p">,</span> <span class="p">[])</span></div><div class='line' id='LC498'><br/></div><div class='line' id='LC499'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span> <span class="o">=</span> <span class="n">fqn</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">)[</span><span class="mi">1</span><span class="p">:]</span> <span class="c"># the first token is always the robot name. Remove it</span></div><div class='line' id='LC500'><br/></div><div class='line' id='LC501'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&quot;Component </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="nb">str</span><span class="p">((</span><span class="n">name</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span> <span class="n">fqn</span><span class="p">,</span> <span class="n">stream</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="n">services</span><span class="p">))</span> <span class="p">)</span></div><div class='line' id='LC502'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cmpt</span> <span class="o">=</span> <span class="n">Component</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span> <span class="n">fqn</span><span class="p">,</span> <span class="n">stream</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="n">services</span><span class="p">)</span></div><div class='line' id='LC503'><br/></div><div class='line' id='LC504'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">name</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span> <span class="c"># this component belongs to the robot directly.</span></div><div class='line' id='LC505'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">robot</span><span class="p">[</span><span class="n">name</span><span class="p">[</span><span class="mi">0</span><span class="p">]]</span> <span class="o">=</span> <span class="n">cmpt</span></div><div class='line' id='LC506'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC507'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">subcmpt</span> <span class="o">=</span> <span class="n">robot</span><span class="p">[</span><span class="n">name</span><span class="p">[</span><span class="mi">0</span><span class="p">]]</span></div><div class='line' id='LC508'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">sub</span> <span class="ow">in</span> <span class="n">name</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">]:</span></div><div class='line' id='LC509'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">subcmpt</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">subcmpt</span><span class="p">,</span> <span class="n">sub</span><span class="p">)</span></div><div class='line' id='LC510'><br/></div><div class='line' id='LC511'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">subcmpt</span><span class="p">,</span> <span class="n">name</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]):</span> <span class="c"># pathologic cmpt name!</span></div><div class='line' id='LC512'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s">&quot;Sub-component name &lt;</span><span class="si">%s</span><span class="s">&gt; conflicts with&quot;</span></div><div class='line' id='LC513'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&lt;</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">&gt; member. To use pymorse with this scenario,&quot;</span></div><div class='line' id='LC514'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;please change the name of the sub-component.&quot;</span> <span class="o">%</span></div><div class='line' id='LC515'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="n">name</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span> <span class="n">subcmpt</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">name</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]))</span></div><div class='line' id='LC516'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">setattr</span><span class="p">(</span><span class="n">subcmpt</span><span class="p">,</span> <span class="n">name</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span> <span class="n">cmpt</span><span class="p">)</span></div><div class='line' id='LC517'><br/></div><div class='line' id='LC518'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">rpc_t</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">,</span> <span class="n">component</span><span class="p">,</span> <span class="n">service</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span></div><div class='line' id='LC519'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">req</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rpc_request</span><span class="p">(</span><span class="n">component</span><span class="p">,</span> <span class="n">service</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span></div><div class='line' id='LC520'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rpc_process</span><span class="p">(</span><span class="n">req</span><span class="p">,</span> <span class="n">timeout</span><span class="p">)</span></div><div class='line' id='LC521'><br/></div><div class='line' id='LC522'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">rpc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">component</span><span class="p">,</span> <span class="n">service</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span></div><div class='line' id='LC523'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; Calls a service from the simulator.</span></div><div class='line' id='LC524'><br/></div><div class='line' id='LC525'><span class="sd">        The call will block until a response from the simulator is received.</span></div><div class='line' id='LC526'><br/></div><div class='line' id='LC527'><span class="sd">        :param component: the component that expose the service (like a robot name)</span></div><div class='line' id='LC528'><span class="sd">        :param service: the name of the service</span></div><div class='line' id='LC529'><span class="sd">        :param args...: (variadic) each service parameter, as a separate argument</span></div><div class='line' id='LC530'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC531'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">req</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rpc_request</span><span class="p">(</span><span class="n">component</span><span class="p">,</span> <span class="n">service</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span></div><div class='line' id='LC532'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rpc_process</span><span class="p">(</span><span class="n">req</span><span class="p">)</span></div><div class='line' id='LC533'><br/></div><div class='line' id='LC534'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_rpc_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">component</span><span class="p">,</span> <span class="n">service</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span></div><div class='line' id='LC535'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">req</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC536'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;id&#39;</span><span class="p">:</span> <span class="s">&#39;</span><span class="si">%i</span><span class="s">&#39;</span><span class="o">%</span><span class="bp">self</span><span class="o">.</span><span class="n">simulator_service_id</span><span class="p">,</span></div><div class='line' id='LC537'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;component&#39;</span><span class="p">:</span> <span class="n">component</span><span class="p">,</span></div><div class='line' id='LC538'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;service&#39;</span><span class="p">:</span> <span class="n">service</span><span class="p">,</span></div><div class='line' id='LC539'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;args&#39;</span><span class="p">:</span> <span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">args</span><span class="p">),</span></div><div class='line' id='LC540'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC541'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">simulator_service_id</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC542'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">req</span></div><div class='line' id='LC543'><br/></div><div class='line' id='LC544'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_rpc_process</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">req</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC545'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">raw</span> <span class="o">=</span> <span class="s">&quot;{id} {component} {service} [{args}]&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">**</span><span class="n">req</span><span class="p">)</span></div><div class='line' id='LC546'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="n">raw</span><span class="p">)</span></div><div class='line' id='LC547'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response_callback</span> <span class="o">=</span> <span class="n">ResponseCallback</span><span class="p">(</span><span class="n">req</span><span class="p">[</span><span class="s">&#39;id&#39;</span><span class="p">])</span></div><div class='line' id='LC548'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">simulator_service</span><span class="o">.</span><span class="n">subscribe</span><span class="p">(</span><span class="n">response_callback</span><span class="o">.</span><span class="n">callback</span><span class="p">)</span></div><div class='line' id='LC549'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC550'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">simulator_service</span><span class="o">.</span><span class="n">publish</span><span class="p">(</span><span class="n">raw</span><span class="p">)</span></div><div class='line' id='LC551'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">with</span> <span class="n">response_callback</span><span class="o">.</span><span class="n">condition</span><span class="p">:</span></div><div class='line' id='LC552'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_up</span><span class="p">()</span> <span class="ow">and</span> <span class="n">response_callback</span><span class="o">.</span><span class="n">condition</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">timeout</span><span class="p">):</span></div><div class='line' id='LC553'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">rpc_get_result</span><span class="p">(</span><span class="n">response_callback</span><span class="o">.</span><span class="n">response</span><span class="p">)</span></div><div class='line' id='LC554'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">finally</span><span class="p">:</span></div><div class='line' id='LC555'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">simulator_service</span><span class="o">.</span><span class="n">unsubscribe</span><span class="p">(</span><span class="n">response_callback</span><span class="o">.</span><span class="n">callback</span><span class="p">)</span></div><div class='line' id='LC556'><br/></div><div class='line' id='LC557'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_up</span><span class="p">():</span></div><div class='line' id='LC558'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">ConnectionError</span><span class="p">(</span><span class="s">&quot;simulation service is down&quot;</span><span class="p">)</span></div><div class='line' id='LC559'><br/></div><div class='line' id='LC560'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">TimeoutError</span><span class="p">(</span><span class="s">&quot;timeout exceeded while waiting for response&quot;</span><span class="p">)</span></div><div class='line' id='LC561'><br/></div><div class='line' id='LC562'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">cancel</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">service_id</span><span class="p">):</span></div><div class='line' id='LC563'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; Send a cancelation request for an existing (running) service.</span></div><div class='line' id='LC564'><br/></div><div class='line' id='LC565'><span class="sd">        If the service is not running or does not exist, the request is</span></div><div class='line' id='LC566'><span class="sd">        ignored.</span></div><div class='line' id='LC567'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC568'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">simulator_service</span><span class="o">.</span><span class="n">publish</span><span class="p">(</span><span class="s">&quot;</span><span class="si">%i</span><span class="s"> cancel&quot;</span><span class="o">%</span><span class="nb">int</span><span class="p">(</span><span class="n">service_id</span><span class="p">))</span></div><div class='line' id='LC569'><br/></div><div class='line' id='LC570'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">close</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cancel_async_services</span> <span class="o">=</span> <span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC571'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">cancel_async_services</span><span class="p">:</span></div><div class='line' id='LC572'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Cancelling all running asynchronous requests...&#39;</span><span class="p">)</span></div><div class='line' id='LC573'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ResponseCallback</span><span class="o">.</span><span class="n">cancel_all</span><span class="p">()</span></div><div class='line' id='LC574'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">executor</span><span class="o">.</span><span class="n">cancel_all</span><span class="p">()</span></div><div class='line' id='LC575'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC576'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Waiting for all asynchronous requests to complete...&#39;</span><span class="p">)</span></div><div class='line' id='LC577'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">executor</span><span class="o">.</span><span class="n">shutdown</span><span class="p">(</span><span class="n">wait</span> <span class="o">=</span> <span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC578'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">simulator_service</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC579'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Close all other asyncore sockets (StreanJSON)</span></div><div class='line' id='LC580'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">asyncore</span><span class="o">.</span><span class="n">close_all</span><span class="p">()</span></div><div class='line' id='LC581'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Morse</span><span class="o">.</span><span class="n">_asyncore_thread</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">TIMEOUT</span><span class="p">)</span></div><div class='line' id='LC582'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Morse</span><span class="o">.</span><span class="n">_asyncore_thread</span> <span class="o">=</span> <span class="bp">None</span> <span class="c"># in case we want to re-create</span></div><div class='line' id='LC583'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Done. Bye bye!&#39;</span><span class="p">)</span></div><div class='line' id='LC584'><br/></div><div class='line' id='LC585'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">spin</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC586'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Morse</span><span class="o">.</span><span class="n">_asyncore_thread</span><span class="o">.</span><span class="n">join</span><span class="p">()</span></div><div class='line' id='LC587'><br/></div><div class='line' id='LC588'><br/></div><div class='line' id='LC589'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#####################################################################</span></div><div class='line' id='LC590'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">###### Predefined methods to interact with the simulator</span></div><div class='line' id='LC591'><br/></div><div class='line' id='LC592'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">quit</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC593'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">rpc</span><span class="p">(</span><span class="s">&quot;simulation&quot;</span><span class="p">,</span> <span class="s">&quot;quit&quot;</span><span class="p">)</span></div><div class='line' id='LC594'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC595'><br/></div><div class='line' id='LC596'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC597'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">rpc</span><span class="p">(</span><span class="s">&quot;simulation&quot;</span><span class="p">,</span> <span class="s">&quot;reset&quot;</span><span class="p">)</span></div><div class='line' id='LC598'><br/></div><div class='line' id='LC599'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">streams</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC600'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">rpc</span><span class="p">(</span><span class="s">&quot;simulation&quot;</span><span class="p">,</span> <span class="s">&quot;list_streams&quot;</span><span class="p">)</span></div><div class='line' id='LC601'><br/></div><div class='line' id='LC602'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_stream_port</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stream</span><span class="p">):</span></div><div class='line' id='LC603'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">rpc</span><span class="p">(</span><span class="s">&quot;simulation&quot;</span><span class="p">,</span> <span class="s">&quot;get_stream_port&quot;</span><span class="p">,</span> <span class="n">stream</span><span class="p">)</span></div><div class='line' id='LC604'><br/></div><div class='line' id='LC605'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">activate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cmpnt</span><span class="p">):</span></div><div class='line' id='LC606'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">rpc</span><span class="p">(</span><span class="s">&quot;simulation&quot;</span><span class="p">,</span> <span class="s">&quot;activate&quot;</span><span class="p">,</span> <span class="n">cmpnt</span><span class="p">)</span></div><div class='line' id='LC607'><br/></div><div class='line' id='LC608'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">deactivate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cmpnt</span><span class="p">):</span></div><div class='line' id='LC609'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">rpc</span><span class="p">(</span><span class="s">&quot;simulation&quot;</span><span class="p">,</span> <span class="s">&quot;deactivate&quot;</span><span class="p">,</span> <span class="n">cmpnt</span><span class="p">)</span></div><div class='line' id='LC610'><br/></div><div class='line' id='LC611'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#### with statement ####</span></div><div class='line' id='LC612'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC613'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span></div><div class='line' id='LC614'><br/></div><div class='line' id='LC615'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_val</span><span class="p">,</span> <span class="n">exc_tb</span><span class="p">):</span></div><div class='line' id='LC616'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">exc_type</span><span class="p">:</span></div><div class='line' id='LC617'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC618'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC619'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">close</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC620'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span> <span class="c"># re-raise exception</span></div><div class='line' id='LC621'><br/></div><div class='line' id='LC622'><span class="k">class</span> <span class="nc">Stream</span><span class="p">(</span><span class="n">asynchat</span><span class="o">.</span><span class="n">async_chat</span><span class="p">):</span></div><div class='line' id='LC623'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; Asynchrone I/O stream handler</span></div><div class='line' id='LC624'><br/></div><div class='line' id='LC625'><span class="sd">    To start the handler, just run :meth asyncore.loop: in a new thread::</span></div><div class='line' id='LC626'><br/></div><div class='line' id='LC627'><span class="sd">    threading.Thread( target = asyncore.loop, kwargs = {&#39;timeout&#39;: .1} ).start()</span></div><div class='line' id='LC628'><br/></div><div class='line' id='LC629'><span class="sd">    where timeout is used with select.select / select.poll.poll.</span></div><div class='line' id='LC630'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC631'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="n">maxlen</span><span class="o">=</span><span class="mi">100</span><span class="p">):</span></div><div class='line' id='LC632'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">error</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC633'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">asynchat</span><span class="o">.</span><span class="n">async_chat</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC634'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">set_terminator</span><span class="p">(</span><span class="n">MSG_SEPARATOR</span><span class="p">)</span></div><div class='line' id='LC635'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">create_socket</span><span class="p">(</span><span class="n">family</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span><span class="p">)</span></div><div class='line' id='LC636'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span> <span class="p">(</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span> <span class="p">)</span></div><div class='line' id='LC637'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_in_buffer</span>  <span class="o">=</span> <span class="n">b</span><span class="s">&quot;&quot;</span></div><div class='line' id='LC638'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_in_queue</span>   <span class="o">=</span> <span class="n">deque</span><span class="p">([],</span> <span class="n">maxlen</span><span class="p">)</span></div><div class='line' id='LC639'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_callbacks</span>  <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC640'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cv_new_msg</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">Condition</span><span class="p">()</span></div><div class='line' id='LC641'><br/></div><div class='line' id='LC642'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">is_up</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC643'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; </span></div><div class='line' id='LC644'><span class="sd">        self.connecting has been introduced lately in several branches</span></div><div class='line' id='LC645'><span class="sd">        of python (see issue #10340 of Python). In particular, it is not</span></div><div class='line' id='LC646'><span class="sd">        present in the python 3.2.3 interpreter delivered in Ubuntu 12.04.</span></div><div class='line' id='LC647'><span class="sd">        On this platform, just test of self.connected. There is still</span></div><div class='line' id='LC648'><span class="sd">        possibly a little race  but it mitigate the issue.</span></div><div class='line' id='LC649'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC650'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s">&#39;connecting&#39;</span><span class="p">):</span></div><div class='line' id='LC651'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">connecting</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">connected</span></div><div class='line' id='LC652'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC653'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">connected</span></div><div class='line' id='LC654'><br/></div><div class='line' id='LC655'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">subscribe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">):</span></div><div class='line' id='LC656'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_callbacks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">callback</span><span class="p">)</span></div><div class='line' id='LC657'><br/></div><div class='line' id='LC658'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">unsubscribe</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">callback</span><span class="p">):</span></div><div class='line' id='LC659'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_callbacks</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">callback</span><span class="p">)</span></div><div class='line' id='LC660'><br/></div><div class='line' id='LC661'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">handle_error</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC662'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">error</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC663'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">handle_close</span><span class="p">()</span></div><div class='line' id='LC664'><br/></div><div class='line' id='LC665'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#### IN ####</span></div><div class='line' id='LC666'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">collect_incoming_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span></div><div class='line' id='LC667'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Buffer the data&quot;&quot;&quot;</span></div><div class='line' id='LC668'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_in_buffer</span> <span class="o">+=</span> <span class="n">data</span></div><div class='line' id='LC669'><br/></div><div class='line' id='LC670'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">found_terminator</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC671'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">handle_msg</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_in_buffer</span><span class="p">)</span></div><div class='line' id='LC672'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_in_buffer</span> <span class="o">=</span> <span class="n">b</span><span class="s">&quot;&quot;</span></div><div class='line' id='LC673'><br/></div><div class='line' id='LC674'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">handle_msg</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg</span><span class="p">):</span></div><div class='line' id='LC675'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; append new raw :param msg: in the input queue</span></div><div class='line' id='LC676'><br/></div><div class='line' id='LC677'><span class="sd">        and call subscribed callback methods if any</span></div><div class='line' id='LC678'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC679'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cv_new_msg</span><span class="p">:</span></div><div class='line' id='LC680'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_in_queue</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span></div><div class='line' id='LC681'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_cv_new_msg</span><span class="o">.</span><span class="n">notify_all</span><span class="p">()</span></div><div class='line' id='LC682'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># handle callback(s)</span></div><div class='line' id='LC683'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">decoded_msg</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC684'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">callback</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_callbacks</span><span class="p">:</span></div><div class='line' id='LC685'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">decoded_msg</span><span class="p">:</span></div><div class='line' id='LC686'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">decoded_msg</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span> <span class="n">msg</span> <span class="p">)</span></div><div class='line' id='LC687'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">callback</span><span class="p">(</span> <span class="n">decoded_msg</span> <span class="p">)</span></div><div class='line' id='LC688'><br/></div><div class='line' id='LC689'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_msg_available</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC690'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_in_queue</span><span class="p">)</span></div><div class='line' id='LC691'><br/></div><div class='line' id='LC692'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_get_last_msg</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC693'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">_in_queue</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="p">)</span></div><div class='line' id='LC694'><br/></div><div class='line' id='LC695'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># TODO implement last n msg decode and msg_queue with hash(msg) -&gt; decoded msg</span></div><div class='line' id='LC696'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">last</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="o">=</span><span class="mi">1</span><span class="p">):</span></div><div class='line' id='LC697'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; get the last message recieved</span></div><div class='line' id='LC698'><br/></div><div class='line' id='LC699'><span class="sd">        :returns: decoded message or None if no message available</span></div><div class='line' id='LC700'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC701'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cv_new_msg</span><span class="p">:</span></div><div class='line' id='LC702'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_msg_available</span><span class="p">():</span></div><div class='line' id='LC703'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_last_msg</span><span class="p">()</span></div><div class='line' id='LC704'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&quot;last: no message in queue&quot;</span><span class="p">)</span></div><div class='line' id='LC705'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">None</span></div><div class='line' id='LC706'><br/></div><div class='line' id='LC707'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC708'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; wait :param timeout: for a new messge</span></div><div class='line' id='LC709'><br/></div><div class='line' id='LC710'><span class="sd">        When the timeout argument is present and not None, it should be a</span></div><div class='line' id='LC711'><span class="sd">        floating point number specifying a timeout for the operation in seconds</span></div><div class='line' id='LC712'><span class="sd">        (or fractions thereof).</span></div><div class='line' id='LC713'><br/></div><div class='line' id='LC714'><span class="sd">        :returns: decoded message or None in case of timeout</span></div><div class='line' id='LC715'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC716'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cv_new_msg</span><span class="p">:</span></div><div class='line' id='LC717'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cv_new_msg</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">timeout</span><span class="p">):</span></div><div class='line' id='LC718'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_last_msg</span><span class="p">()</span></div><div class='line' id='LC719'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s">&quot;get: timed out&quot;</span><span class="p">)</span></div><div class='line' id='LC720'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">None</span></div><div class='line' id='LC721'><br/></div><div class='line' id='LC722'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#### OUT ####</span></div><div class='line' id='LC723'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">publish</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg</span><span class="p">):</span></div><div class='line' id='LC724'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; encode :param msg: and append the resulting bytes to the output queue &quot;&quot;&quot;</span></div><div class='line' id='LC725'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span> <span class="n">msg</span> <span class="p">))</span></div><div class='line' id='LC726'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#### patch code from asynchat, ``del deque[0]`` is not safe #####</span></div><div class='line' id='LC727'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">initiate_send</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC728'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">producer_fifo</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">connected</span><span class="p">:</span></div><div class='line' id='LC729'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">producer_fifo</span><span class="o">.</span><span class="n">popleft</span><span class="p">()</span></div><div class='line' id='LC730'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># handle empty string/buffer or None entry</span></div><div class='line' id='LC731'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">first</span><span class="p">:</span></div><div class='line' id='LC732'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">first</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC733'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">handle_close</span><span class="p">()</span></div><div class='line' id='LC734'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC735'><br/></div><div class='line' id='LC736'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># handle classic producer behavior</span></div><div class='line' id='LC737'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">obs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ac_out_buffer_size</span></div><div class='line' id='LC738'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC739'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="n">first</span><span class="p">[:</span><span class="n">obs</span><span class="p">]</span></div><div class='line' id='LC740'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">TypeError</span><span class="p">:</span></div><div class='line' id='LC741'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="n">first</span><span class="o">.</span><span class="n">more</span><span class="p">()</span></div><div class='line' id='LC742'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">data</span><span class="p">:</span></div><div class='line' id='LC743'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">producer_fifo</span><span class="o">.</span><span class="n">appendleft</span><span class="p">(</span><span class="n">data</span><span class="p">)</span></div><div class='line' id='LC744'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC745'><br/></div><div class='line' id='LC746'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_encoding</span><span class="p">:</span></div><div class='line' id='LC747'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">encoding</span><span class="p">)</span></div><div class='line' id='LC748'><br/></div><div class='line' id='LC749'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># send the data</span></div><div class='line' id='LC750'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC751'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">num_sent</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="n">data</span><span class="p">)</span></div><div class='line' id='LC752'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="n">socket</span><span class="o">.</span><span class="n">error</span><span class="p">:</span></div><div class='line' id='LC753'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">handle_error</span><span class="p">()</span></div><div class='line' id='LC754'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC755'><br/></div><div class='line' id='LC756'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">num_sent</span><span class="p">:</span></div><div class='line' id='LC757'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">num_sent</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span> <span class="ow">or</span> <span class="n">obs</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">first</span><span class="p">):</span></div><div class='line' id='LC758'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">producer_fifo</span><span class="o">.</span><span class="n">appendleft</span><span class="p">(</span><span class="n">first</span><span class="p">[</span><span class="n">num_sent</span><span class="p">:])</span></div><div class='line' id='LC759'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># we tried to send some actual data</span></div><div class='line' id='LC760'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC761'><br/></div><div class='line' id='LC762'><br/></div><div class='line' id='LC763'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#### CODEC ####</span></div><div class='line' id='LC764'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">decode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg_bytes</span><span class="p">):</span></div><div class='line' id='LC765'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; decode bytes to string &quot;&quot;&quot;</span></div><div class='line' id='LC766'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">msg_bytes</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span></div><div class='line' id='LC767'><br/></div><div class='line' id='LC768'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">encode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg_str</span><span class="p">):</span></div><div class='line' id='LC769'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; encode string to bytes &quot;&quot;&quot;</span></div><div class='line' id='LC770'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">msg_str</span><span class="o">.</span><span class="n">encode</span><span class="p">()</span> <span class="o">+</span> <span class="n">MSG_SEPARATOR</span></div><div class='line' id='LC771'><br/></div><div class='line' id='LC772'><span class="k">class</span> <span class="nc">StreamJSON</span><span class="p">(</span><span class="n">Stream</span><span class="p">):</span></div><div class='line' id='LC773'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="n">maxlen</span><span class="o">=</span><span class="mi">100</span><span class="p">):</span></div><div class='line' id='LC774'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Stream</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="n">maxlen</span><span class="p">)</span></div><div class='line' id='LC775'><br/></div><div class='line' id='LC776'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">decode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg_bytes</span><span class="p">):</span></div><div class='line' id='LC777'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; decode bytes to json object &quot;&quot;&quot;</span></div><div class='line' id='LC778'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">Stream</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg_bytes</span><span class="p">))</span></div><div class='line' id='LC779'><br/></div><div class='line' id='LC780'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">encode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">msg_obj</span><span class="p">):</span></div><div class='line' id='LC781'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; encode object to json string and then bytes &quot;&quot;&quot;</span></div><div class='line' id='LC782'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Stream</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">msg_obj</span><span class="p">))</span></div></pre></div>
            </td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2013 <span title="0.05315s from github-fe125-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/morse-simulator/morse/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

  </body>
</html>

