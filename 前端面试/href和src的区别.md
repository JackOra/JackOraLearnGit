### href和src的区别



#### **src用于替换当前元素，href用于在当前文档和引用资源之间确立联系**

src是source的缩写，**指向外部资源的位置，指向的内容将会嵌入到文档中当前标签所在位置；**

当浏览器解析到该元素时，**会暂停其他资源的下载和处理**，直到将该资源加载、编译、执行完毕，图片和框架等元素也如此，类似于将所指向资源嵌入当前标签内。**这也是为什么将js脚本放在底部而不是头部**。

### 阻塞渲染

​	**然后当浏览器在解析到 script 标签时，会暂停构建 DOM ，完成后才会从暂停的地⽅重** 

**新开始。也就是说，如果你想⾸屏渲染的越快，就越不应该在⾸屏就加载 JS ⽂件，这也** 

**是都建议将 script 标签放在 body 标签底部的原因。**

href是Hypertext Reference的缩写，指向网络资源所在位置，**建立和当前元素（锚点）或当前文档（链接）之间的链接**，如果我们在文档中添加(如下图)，那么浏览器会识别该文档为css文件，**就会并行下载资源并且不会停止对当前文档的处理**。这也是为什么建议使用link方式来加载css，而不是使用@import方式。常用的有link和a标签。（引用）

