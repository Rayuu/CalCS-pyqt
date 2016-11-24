# CalCS-pyqt

##  一个计算CS和的界面程序

```
	/******************************************************************
	*校验码 将所有相加MOD 256 
	*******************************************************************/
	uchar Get_csckNum( uchar *Ptr, uchar Len )
	{
	    uchar Num;
	        
	    Num = 0;
	    while( Len > 0 )
	    {
	    Num += *Ptr;
	    	Ptr++;
	    	Len--;
	    }
	    return Num;
	}

```

[http://www.cnblogs.com/doudongchun/p/3694765.html](http://www.cnblogs.com/doudongchun/p/3694765.html)

[http://www.cnblogs.com/doudongchun/p/3694786.html](http://www.cnblogs.com/doudongchun/p/3694786.html)
