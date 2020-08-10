# coding:utf-8 
#!/usr/bin/env python
seq=input("请输入序列：")
seqq=seq.lower()
table=str.maketrans('atcg','tagc')
print("其互补链为:",seqq.translate(table))
reseq=seqq.translate(table)
print("其反向互补链为:",reseq[::-1])
input("敲击回车退出")
