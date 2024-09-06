val scala3Version = "3.4.1"

lazy val root = project
  .in(file("."))
  .settings(
    name := "wordle",
    version := "0.1.0-SNAPSHOT",

    scalaVersion := scala3Version,
    
    libraryDependencies += "org.typelevel" %% "cats-core" % "2.10.0"
  )
