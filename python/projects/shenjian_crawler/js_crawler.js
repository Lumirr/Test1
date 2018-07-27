var configs = {
  domains : ["bbs.tianya.cn"],
  scanUrls: ["http://bbs.tianya.cn/hotArticle.jsp"],
  contentUrlRegexes : [],
  helperUrlRegexes : [/http:\/\/bbs\.tianya\.cn\/hotArticle\.jsp(\?pn=\d+)?/],
  fields : [
    {
      name: "items",
      selector : "//table[contains(@class,'tab-bbs-list')]/tbody/tr",//每项都是数组
      repeated : true,
      children : [
        {
          name : "title",
          alias : "标题",
          selector : "//td[@class='td-title']/a",
          //selector: "//div[@id='main']/div[@class='mt5']/table[@class='tab-bbs-list tab-bbs-list-2']//td[@class='td-title']/a",////*[@id="main"]/div[2]/table/tbody[2]/tr[1]/td[1]/a
          required : true
        },
        {
          name: "author",
          alias : "作者",
          selector : "//a[@class='author']"//这是相对父路径的。
          //selector: "//div[@id='main']/div[@class='mt5']/table[@class='tab-bbs-list tab-bbs-list-2']//a[@class='author']"
        },
        {
          name : "replied_time",
          alias : "回复时间",
          selector : "//td[3]"
          //selector : "//div[@id='main']/div[@class='mt5']/table[@class='tab-bbs-list tab-bbs-list-2']/tbody/td[3]"
        }
      ]
  }]
};

configs.onProcessScanPage = function (page, content, site) {
  return false;
};

configs.onProcessHelperPage = function (page, content, site) {
  var nextUrl = extract(content, "//div[@id='main']/div[3]//a[text()='下页']/@href");////*[@id="main"]/div[3]/a[7]
  if (nextUrl != null) 
    site.addUrl(nextUrl);
  return false;
};

configs.afterExtractField = function (fieldName, data, page, site) {
  if ('items.replied_time' == fieldName ) {
    var timestamp = parseDateTime(data);
    return isNaN(timestamp)? 0: timestamp;
  }
  return data;
};

configs.onProcessContentPage = function (page, content, site) {
  return false;
};

var crawler = new Crawler(configs);
crawler.start();
