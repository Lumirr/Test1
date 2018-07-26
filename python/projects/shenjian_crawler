/*
var configs = {
  domains : ["wandoujia.com"],
  scanUrls: ['http://apps.wandoujia.com/api/v1/apps?type=weeklytopgame&max=12&start=0'],
  helperUrlRegexes: [/http:\/\/www\.wandoujia\.com\/api\/v1\/apps\?type=weeklytopgame&max=12&start=\d+/],
  */
//  contentUrlRegexes : [/http[s:\/]www\.wandoujia\.com\/apps\/.*/],
/*
  fields : [
    {
      name:'game_name',
      alias : "游戏名",
      selector : "//span",
  }]
}
var crawler = new Crawler(configs);
crawler.start();
*/
var configs = {
    domains: ["wandoujia.com"],
    scanUrls: ["http://apps.wandoujia.com/api/v1/apps?type=weeklytopgame&max=12&start=0"],
    contentUrlRegexes: [/http:\/\/www\.wandoujia\.com\/apps\/.*/],
    helperUrlRegexes: [/http:\/\/apps\.wandoujia\.com\/api\/v1\/apps\?type=weeklytopgame&max=12&start=\d+/],
    fields: [
        {
            name: "game_name",
            alias: "游戏名",
            selector : "//div/p/span[@class='title']",
            //selector: "//span[contains(@class,'title')]",
            required: true 
        },
        {
            name: "game_download",
            alias: "下载量",
            selector: "//div/span[@class='item install']/i"
            //selector: "//i[@itemprop='interactionCount']"
        },
        {
            name:"game_icon",
            alias: "游戏图标",
            selector: "//div[@class='detail-top clearfix']/div[@class='app-icon']/img/@src"
            //selector:"//div[contains(@class,'app-icon')]/img[@itemprop='image']/@src"
        }
        
    ]
};

configs.onProcessScanPage = function (page, content, site) {
    //取消自动从入口页发现新链接
    return false;
};

/*
  回调函数onProcessHelperPage：获取下一页列表页以及从列表页中获取内容页链接，并手动添加到待爬队列中
*/
configs.onProcessHelperPage = function(page, content, site) {
  var jsonContent = JSON.parse(content);
  console.log(jsonContent.length);
  for (var i=0, j=jsonContent.length; i<j; i++) {
    var newUrl = "http://www.wandoujia.com/apps/"+jsonContent[i].packageName;
    site.addUrl(newUrl);
  }
  //只取排行榜前100的游戏
  var start = parseInt(page.url.substring(page.url.indexOf("&start=") + 7));
  var currentStart = start + 12;
  if (currentStart < 100) {
    site.addUrl("http://apps.wandoujia.com/api/v1/apps?type=weeklytopgame&max=12&start=" + currentStart);
  }
  return false;
}
  
  
  
    /*
    // 列表页返回的数据是json，需要先转换成json格式
    var jarr = JSON.parse(content);
    // 从json数组中获取内容页链接并添加到待爬队列中
    for (var i = 0, n = jarr.length; i < n; i++) {
      console.log(jarr.length)
      var new_url = "http://www.wandoujia.com/apps/"+jarr[i].packageName;
      site.addUrl(new_url);
    }
    // 获取下一页列表页链接并添加到待爬队列中
    var currentStart = parseInt(page.url.substring(page.url.indexOf("&start=") + 7));
    var start = currentStart+12;
    if(start < 100){ // 该demo只爬取游戏排行榜前100的游戏
      site.addUrl("http://apps.wandoujia.com/api/v1/apps?type=weeklytopgame&max=12&start="+start);
    }
    return false; // 返回false表示不从当前列表页中自动发现新的链接，从而避免添加无用的链接，提高爬取速度
    };
    */

configs.onProcessContentPage = function (page, content, site) {
    //取消自动从内容页发现新链接
    return false;
};

var crawler = new Crawler(configs);
crawler.start();
