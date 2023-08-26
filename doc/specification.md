
Interface Customizer:
-v|--verbose:
Show all output in the terminal.
-q|--quiet:
SEE
	Only show Customizer’s prints in the terminal and do not show output from commands.
-Q|--Quiet:
	Do not show any output in the terminal.

-s|--skip|--skip-if-installed:
	
-o|--overwrite|--overwrite-if-present:
	
void initializations()


void featureDataParser(String keyName)

# Description: Fill a data structure having all features you want to install
void argumentParser(List<String> arguments):

Class CustomizerImpl implements Customizer

dict <String, Feature> features 
List <Feature> installationFeatures
Runtime runtime

Interface Logger:
void info(String msg):

void warning(String msg):

void error(String msg):


Interface SystemAPI:
void enablePrint()

void disablePrint()

void bellSound()

void removeFile(Path filePath) throws FileNotFoundException, DeniedException

void removeFolder(Path folderPath) throws FolderNotFoundException, DeniedException

String getOSName()
SEE

void customPermission(String user, Path folderPath)
void applyPermissionsRecursively(String user, Path folderPath)

void createFile(Path filePath, String fileContent)

void createFile(Path filePath, Path fileContent)

void createFolder(Path folderPath)

void copyLauncher(Path launcherPath)

void createLinks(Path filePath, String commandName)

void decompress(Path filePath, String folderName)

void decompress(Path filePath, Path folderPath)

void download(String url, Path filePath)

void registerFileAssociations(MimeType fileType, Path desktopLauncherPath)

void addGpgSignature(String url)

void addAptSource(String url)

void moveFiles(Path originFilePath, Path destinyFilePath)

void cloneRepository(String url, Path filePath)

Interface Cache:
Bool isCached(Runtime runtime, FileWrapper fileWrapper)

void cacheFile(FileWrapper fileWrapper, Path filePath)

void flushCache(FileWrapper fileWrapper, String fileName)

void flushCacheFile(FileWrapper fileWrapper, String fileName)


Interface PythonVirtualEnvironment:
void createPythonVirtualEnvironment()
void installPipPackage()
void installPythonPackage()
void uninstallPipPackage()
void uninstallPythonPackage()
void upgradePip()
void installWheelPackage()


Interface Feature:
# @delegates to isInstalled
Bool isInstalled(Runtime runtime)

void install(Runtime runtime)

void uninstall(Runtime runtime)

Static Bool isInstalled(Runtime runtime, Feature feature)
Static Bool isInstalled(Runtime runtime, String feature)

Path getInstallationFolder(Runtime runtime)
Class FeatureImpl implements Feature

String name
String description
String version
List<String> tags
List<String> arguments
List<Systemcategories> systemcategories
FeatureImpl(Runtime runtime) {
# Read properties from file
}

Enum Systemcategories

Interface InstallationOption:
void install(Runtime runtime)

void uninstall(Runtime runtime)

Class InstallationOptionImpl implements InstallationOption
List<Task> tasks
Bool isPrivileged()

Interface Task:
void do(Runtime runtime)

void undo(Runtime runtime)

Class DesktopLauncher implements Task
# @Inherits do, undo
private String dynamicLauncherDeduceExec(String launcherKeyname)
private String dynamicLauncherDeduceIcon(String launcherKeyname)
private String getDynamicLauncher(String launcherKeyname)
private String createWSL2DynamicLauncher(String launcherKeyname)


Class BashFunction implements Task
File bashFunctionContent
String bashFunctionName

Class BashInitialization implements Task
File bashInitializationContent
String bashInitializationName

Class KeyBinding implements Task
File keyBindingKeyCombination
String keyBindingKeyCombinationName

Class Favorite implements Task
DesktopLauncher favoriteDesktopLauncherName

Class Autostart implements Task
DesktopLauncher autostartDesktopLauncherName

Class FileAssociation implements Task
DesktopLauncher fileAssociationDesktopLauncherName

Class LinkInPath implements Task
Path fileToLinkPath
String fileToLinkName


Interface Runtime:
Flags getFlags()
Feature getCurrentFeature()
# @delegates to CurrentFeature 
Path getCurrentFeatureInstallationFolder()
Bool isRoot()

PackageManager packageManager

Class Common
Path getProjectFolder()
Path getInstallationFolder()

Class FileWrapper
Path filePath
void translateVariables()
void applyPermission(String userName, String userGroup, String mask)
void removeText(String textToBeRemoved) throws Exceptions
void appendText(String textToBeAppended) throws Exceptions

Interface PackageManager:
void install(List<String>packages)
void uninstall(List<String>packages)
void clean()
void update()

Class AptGet implements packageManager
Class Dnf implements packageManager
Class Pkg implements packageManager

Class Flags
dict<String, Int> flags

Class Installation
Flags flags
InstallationOption installationOption

Interface CustomizerAPI:
void addBashFunction(String bashFunctionContent, String bashFunctionName, Path relativePath)

void addBashInitialization(String bashInitializationContent, String bashInitializationName, Path relativePath)

void createFolderForCurrentUser(Path folderPath)

void createLinksInPath(Path filePath, String commandName)

void createManualLauncher(String launcherContent, String LauncherName)