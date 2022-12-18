### DTD
Document Tpe Definition is to define the legal building blocks of an XML.
- A DTD defines the document structure with a list of legal elements and attributes.
- Describes teh format of the XML

An internal DTD is declared inside the XML file within a DOCTYPE definition.
```dtd
<!DOCTYPE customer [
        <!ELEMENT customer (firstname, lastname, address, sex, phone, email)>
        <!ELEMENT firstanme (#PCDATA)>
        <!ELEMENT lastname (#PCDATA)>
        <!ELEMENT address (street, city, state, zip, country)>
        ...
]>
```
An externally defined DTD is declared within DOCTYPE definition.
```xml
<?xml version="1.0"?>
<!DOCTYPE customer SYSTEM "customer.dtd">
<!-- customer.dtd contains the definition of the format of the XML document -->
```
DTD element operator allow fine-grain control of the XML document's definition:
+ one or more occurrences of the child
* zero or more occurrences of the child
? zero or one occurrence of the child
| either/Or one of the listed child elements
‘ used to separate elements in a sequence

- An XML element may be defined to be EMPTY.
- An XML element may be defined to be of ANY type.
- An XML element may be defined as containing parsed character data with #PCDATA
___
## Example of DTD
```xml
<?xml version="1.0" encoding="UTF-8"?> <!-- Declaration line -->
<!DOCTYPE CATALOG SYSTEM "cd_catalog.dtd"> <!--Definition of DTD -->
<catalog>
    <CD>
        <TITLE>The Dark Side of the Moon</TITLE>
        <ARTIST>Pink Floyd</ARTIST>
        <COUNTRY>USA</COUNTRY>
        <COMPANY>Capital Records</COMPANY>
        <PRICE>12.99</PRICE>
        <COST>5.99</COST>
        <YEAR>1973</YEAR>
    </CD>
    <CD>
        <TITLE>Still got the blues</TITLE>
        <ARTIST>Gary Moore</ARTIST>
        <COUNTRY>UK</COUNTRY>
        <COMPANY>Virgin records</COMPANY>
        <PRICE>10.20</PRICE>
        <YEAR>1990</YEAR>
    </CD>
</catalog>
```
DTD file in the same folder
```dtd
<!ELEMENT CATALOG (CD*)>
<!ELEMENT CD (TITLE,ARTIST,COUNTRY,COMPANY,PRICE?,COST,YEAR,INVENTORY?,BIN?)>
<!ELEMENT TITLE (#PCDATA)>
<!ELEMENT ARTIST (#PCDATA)>
<!ELEMENT COUNTRY (#PCDATA)>
<!ELEMENT COMPANY (#PCDATA)>
<!ELEMENT PRICE (#PCDATA)>  
<!ELEMENT COST (#PCDATA)>
<!ELEMENT YEAR (#PCDATA)>
<!ELEMENT INVENTORY (#PCDATA)>
<!ELEMENT BIN (#PCDATA)>
```
___
## Attribute
To declare attributes in DTD use the ATTLIST declaration.  
```dtd
<!ATTLIST element-name attribute-name attribute-type attribute-value>
```
Use a single <!ATTLIST> declaration to declare all attributes for a given element.

Default values for an attribute may be provided in the declaration.  
```dtd
<!ATTLIST element_name attribute_name CDATA "default_value">
```


## Sources
- [w3schools](https://www.w3schools.com/XML/default.asp)
- Simon Sez IT, [Learn XML Crash Course: Discover Essential XML Fundamentals](https://www.udemy.com/course/learn-xml-crash-course/)


