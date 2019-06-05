```sql
--odps sql 
--********************************************************************--
--author:booboo
--create time:2019-05-17 10:28:08
--********************************************************************--
SELECT 
        cloud_resource_account
        ,'2019-05-05 00:00:00' request_time
        ,round(sum(invoice_price),2)
        ,round(sum(tax_free_amount),2)
        ,round(sum(tax_amount),2)
        ,WM_CONCAT(invoice_ids,',')
FROM    cloud_resource_invoice_request
group by cloud_resource_account
;
``

* WM_CONCAT()
* group_concat()
