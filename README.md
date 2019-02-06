SnapPy
---

This is a light weight Python code use for replacing your Maven POM Snapshot Version with your github organization and branch name which runs on a Docker Container.

I have use Team_foo as organization & Bar as a branch name but, you can replace it according to your organization & branch name in the below line.

```
newVersion = xml_to_check.replace('SNAPSHOT','ci_Team_Foo_Bar-SNAPSHOT')
```

Once, you are good with name. You can build the image using below command 

```
docker build -t imagename .
```
Once, image is build you can run the container using the below command

```
docker run -it --name containername imagename
```

**Sample Output**

```

 XML well formed, syntax ok.

 Snapshot Found...

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.wsi.devops</groupId>
  <artifactId>python-test</artifactId>
  <version>1.0-ci_Team_Foo_Bar-SNAPSHOT</version>
</project>
```
