# COVID-19 Apps 

These are already made and developed tools which can be grabbed and embedded into your own websites without having to go through much of the development proceess. 

These apps include: 

- Dashboards
- Finder Apps 
- Crowd-Sourcing Tools
- Public Outreach and Story Telling 

Currently and still _in development progress_ our [Consolidated Tool](https://experience.arcgis.com/experience/5b8ed3a1cde64d60a5a0de3267a7e865/page/page_0/) will house the most used tools which can be accessed on the goal. 

## Dashboards 

Dashboards are mainly built on the data that we update on a regular basis (daily) depending on the arrival of the latest update from our data sources. 

The main dashboards available for public use are: 

- Infections Dashboard
- Vaccination Progress Dashboard

We have also developed individual dashboards which also provide focused analytics for the specified theme or title. These are: 

- Provincial tracker
- PCR testing tracker

and also another repetition of the

- infections and 
- vaccination dashboards 

but this time with reduced information to avoid cluttering. 

## Embedding The Dashboards

Embedding these dashboards is prettty easy. No programming knowledge is required here just a `copy` and `paste` action. Anyone can embed these either in Mobile or Web based applications. 

**Where these have been embedded?** 

Check out how [_Pindula_](https://news.pindula.co.zw/coronavirus) and the [_Ministry of Health and Child Care of Zimbabwe (MoHCC)_](http://pillars.mohcc.org.zw:2020/covid19-pillars/) have embedded these on their websites

### Dashboard URL's

The dashboards can be accessible via URL's over the WWW. These URLs;

**Main Dashboards**

- Infections (Desktop only) 

`https://surveyor-jr.maps.arcgis.com/apps/opsdashboard/index.html#/8ef907d2658c44c6a143819aa7979b20`


- Infections (Mobile only) 

`https://surveyor-jr.maps.arcgis.com/apps/dashboards/34d90727cc5548dab0bd6cce8db04595`


- Infections (Mobile Responsive) 

`https://experience.arcgis.com/experience/e6eb41418ae14567a41d9bd9c26fcb06/`

- Vaccination (Desktop Only)

`https://surveyor-jr.maps.arcgis.com/apps/dashboards/f8e4092e67ae4e0a83b73e0756bd793a`


- Vaccination (Mobile Only) 

`https://surveyor-jr.maps.arcgis.com/apps/dashboards/322c36f5e87b47c1b0ea761f8d8315f2`

**Thematic Dashboards** 

All these are still in _Desktop_ mode. 

- Infections 

`https://surveyor-jr.maps.arcgis.com/apps/dashboards/83fef49165d34acbbcfe36f755e0e745`

- Vaccination 

`https://surveyor-jr.maps.arcgis.com/apps/dashboards/1179bbef36fd4f21977096e4f29265a2`

- Provincial Tracker 

`https://surveyor-jr.maps.arcgis.com/apps/dashboards/2d644045633843499ad61bb6a4519f57`

- PCR Test Tracker 

`https://surveyor-jr.maps.arcgis.com/apps/dashboards/878443b3cfb7422899c7b4076b7dbf94`

### Basic HTML Website

For embedding in a basic website, copy the code block below and replace with the appropiate URL for the exact Dashboard you need. 

```HTML
    <style>.embed-container {
        position: relative; 
        padding-bottom: 80%; 
        height: 0; 
        max-width: 100%;
        } .embed-container iframe, .embed-container object, .embed-container iframe{
            position: absolute; 
            top: 0; 
            left: 0; 
            width: 100%; 
            height: 100%;
            } small{
                position: absolute; 
                z-index: 40; 
                bottom: 0; 
                margin-bottom: -15px;
                }
    </style>
    <div class="embed-container">
        <iframe width="500" 
            height="400" 
            frameborder="0" 
            scrolling="no" 
            marginheight="0" 
            marginwidth="0" 
            title="COVID-19" 
            src="<dashboard_url_here>">
        </iframe>
    </div>

```

Replace `dashboard_url_here` with the intended Dashboard URl from the list above. 

Feel free and do not hesitate to edit the styling. The one provided is just the basic styling that makes a perfecct fit for a good wide screen display. 

### Wordpress Site

For a WordPress website, you might want to match the wordpress conventions and prevent unneccesry errors in case Wordpress source code gets updated and a couple of things change. 

Just to be on the right side and stay safe we recommed placing this as a `post`. The code for embedding: 

```HTML
    <article id="post-<your_page_id>" class="post-<your_page_id> page type-page status-publish hentry">
	<header class="entry-header">
		<h1 class="entry-title">Covid-19 Dashboard</h1>	</header><!-- .entry-header -->
	    <div class="entry-content">
            <iframe src="<dashboard_url_here>" 
                frameborder="0" 
                style="overflow:hidden;
                height:100vh;
                width:100vw" 
                height="100%" 
                width="100%">
            </iframe>
			</div><!-- .entry-content -->
    </article>
    <!-- #post-## -->
```

Just like before, replace the `dashboard_url_here` with the actual URL to the dashboard provided above. 

Here we have added another parameter to be replaced, `your_page_id`. If you go through the normal process of creating a post in Wordpress this section is already filled for you by default hence you can begin from the `iframe`.

In case you are a bit handy with your wordpress, __DO NOT__ forget the _page ID_ component. 

## Finder Apps/Tools

A set of tools based on location intelligence. They help users find resources within their vicinity and prevent you from running around places when you can minimise costs and get them close to you. 

- vaccination center finder
- testing center finder _(still in development)_
- quaratine center finder
- isolation and treatment facility finder

## Embedding Finder Apps/Tools

Just like the dashboards, these can also be embedded. 

**Best Practice** 

For efficiency, _geolocation_ is a crucial and essential component in order for these to work hence Geolocation should be enabled. 

When using an `iframe` then;

```
<iframe src="<app_url>" allow="geolocation"></iframe>
```

should be used. 

### Apps URLs

Location intelligent applications are well placed within our [COVID-19 Hub for Zimbabwe](https://covid19.africansurveyors.net/). You can also do the same for your website by simply using the links which directly link to the application or tool. 

- vaccination center finder 

`https://africageoportal.maps.arcgis.com/apps/webappviewer/index.html?id=1bab4a7388d449c08b0cbc6765c83389`

- quarantine center finder 

`https://r183992v.maps.arcgis.com/apps/webappviewer/index.html?id=8fcfc239f53c4893b71b434d340667c1`

- isolation and treatment center finder

`https://r183992v.maps.arcgis.com/apps/webappviewer/index.html?id=e382f51eb66b4c5db0e1ada0b0abf630`

__Disclaimer Note__: The Quarantine and Isolation &amp; Treatment Center find applications have not been mantained for a while due to unavailability of reliable data sources hence we do not entirely gurantee their full functionality.

We also recommend using these applications from the source. This steps below will take you through on how you can host these applications on your own website server. 

## Apps from Source

Instead of embedding these applications, perhaps hosting the source code on your servers is the best practice which it is. 

1. Navigate to the [applications source code repository](https://github.com/Surveyor-Jr/Zimbabwe-COVID-19-Data-Center-Resources)
2. Fork the Repo
3. `git clone` into your local system 
4. upload to your server

Source Credits: [ArcGIS Developers](https://developers.arcgis.com/)

In case you want to edit the source code based on your skills, kindly refer to the [Web App Builder Docs](https://developers.arcgis.com/web-appbuilder/api-reference/app-configuration.htm%22%3EJSON) since we do not entirely own this. 

## Issues

Much of the work has been covered but due to time and reosurces, there a some issues which we hope to sort out in the next coming weeks or months depending on availability. 

- mobile responsiveness. 

_Some of the dashboards have mobile responsive alternatives but much of the __Thematics__ Dashboards are still in Desktop version ONLY at the current moment_ 

- data records for location applications

_The data records for the location based applications is at times inaccessible for the general public. Some of the tools (i.e Quarantine Center Find and the Isolation and treatment center finder) have been deprecated due to these reasons._

We however hope to engage relevant authorities and be able to fix this data and information gap. 