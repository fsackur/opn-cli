from opnsense_cli.api.base import ApiBase


class Activity(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "activity"
    """
    Diagnostics ActivityController
    """

    @ApiBase.get
    def getActivity(self, *args):
        self.command = "getActivity"


class Cpu_usage(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "cpu_usage"
    """
    Diagnostics Cpu_usageController
    """

    @ApiBase.get
    def getCPUType(self, *args):
        self.command = "getCPUType"

    @ApiBase.get
    def stream(self, *args):
        self.command = "stream"


class Dns(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "dns"
    """
    Diagnostics DnsController
    """

    @ApiBase.get
    def reverseLookup(self, *args):
        self.command = "reverseLookup"


class Dns_diagnostics(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "dns_diagnostics"
    """
    Diagnostics Dns_diagnosticsController
    """

    @ApiBase.get
    def get(self, *args):
        self.command = "get"

    @ApiBase.get
    def set(self, *args):
        self.command = "set"

    @ApiBase.post
    def set(self, *args):
        self.command = "set"


class Firewall(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "firewall"
    """
    Diagnostics FirewallController
    """

    @ApiBase.post
    def delState(self, stateid, creatorid, *args):
        self.command = "delState"

    @ApiBase.post
    def flushSources(self, *args):
        self.command = "flushSources"

    @ApiBase.post
    def flushStates(self, *args):
        self.command = "flushStates"

    @ApiBase.post
    def killStates(self, *args):
        self.command = "killStates"

    @ApiBase.get
    def listRuleIds(self, *args):
        self.command = "listRuleIds"

    @ApiBase.get
    def log(self, *args):
        self.command = "log"

    @ApiBase.get
    def logFilters(self, *args):
        self.command = "logFilters"

    @ApiBase.get
    def pfStates(self, *args):
        self.command = "pfStates"

    @ApiBase.get
    def pfStatistics(self, *args, section=None):
        self.command = "pfStatistics"

    @ApiBase.post
    def queryPfTop(self, *args):
        self.command = "queryPfTop"

    @ApiBase.post
    def queryStates(self, *args):
        self.command = "queryStates"

    @ApiBase.get
    def stats(self, *args):
        self.command = "stats"

    @ApiBase.get
    def streamLog(self, *args):
        self.command = "streamLog"


class Interface(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "interface"
    """
    Diagnostics InterfaceController
    """

    @ApiBase.post
    def CarpStatus(self, status, *args):
        self.command = "CarpStatus"

    @ApiBase.post
    def delRoute(self, *args):
        self.command = "delRoute"

    @ApiBase.post
    def flushArp(self, *args):
        self.command = "flushArp"

    @ApiBase.get
    def getArp(self, *args):
        self.command = "getArp"

    @ApiBase.get
    def getBpfStatistics(self, *args):
        self.command = "getBpfStatistics"

    @ApiBase.get
    def getInterfaceConfig(self, *args):
        self.command = "getInterfaceConfig"

    @ApiBase.get
    def getInterfaceNames(self, *args):
        self.command = "getInterfaceNames"

    @ApiBase.get
    def getInterfaceStatistics(self, *args):
        self.command = "getInterfaceStatistics"

    @ApiBase.get
    def getMemoryStatistics(self, *args):
        self.command = "getMemoryStatistics"

    @ApiBase.get
    def getNdp(self, *args):
        self.command = "getNdp"

    @ApiBase.get
    def getNetisrStatistics(self, *args):
        self.command = "getNetisrStatistics"

    @ApiBase.get
    def getPfsyncNodes(self, *args):
        self.command = "getPfsyncNodes"

    @ApiBase.get
    def getProtocolStatistics(self, *args):
        self.command = "getProtocolStatistics"

    @ApiBase.get
    def getRoutes(self, *args):
        self.command = "getRoutes"

    @ApiBase.get
    def getSocketStatistics(self, *args):
        self.command = "getSocketStatistics"

    @ApiBase.get
    def getVipStatus(self, *args):
        self.command = "getVipStatus"

    @ApiBase.get
    def searchArp(self, *args):
        self.command = "searchArp"

    @ApiBase.get
    def searchNdp(self, *args):
        self.command = "searchNdp"


class Lvtemplate(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "lvtemplate"
    """
    Diagnostics LvtemplateController
    """

    @ApiBase.post
    def addItem(self, *args):
        self.command = "addItem"

    @ApiBase.post
    def delItem(self, uuid, *args):
        self.command = "delItem"

    @ApiBase.get
    def get(self, *args):
        self.command = "get"

    @ApiBase.get
    def getItem(self, *args, uuid=None):
        self.command = "getItem"

    @ApiBase.*
    def searchItem(self, *args):
        self.command = "searchItem"

    @ApiBase.post
    def set(self, *args):
        self.command = "set"

    @ApiBase.post
    def setItem(self, uuid, *args):
        self.command = "setItem"


class Netflow(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "netflow"
    """
    Diagnostics NetflowController
    """

    @ApiBase.get
    def cacheStats(self, *args):
        self.command = "cacheStats"

    @ApiBase.get
    def getconfig(self, *args):
        self.command = "getconfig"

    @ApiBase.get
    def isEnabled(self, *args):
        self.command = "isEnabled"

    @ApiBase.post
    def reconfigure(self, *args):
        self.command = "reconfigure"

    @ApiBase.get
    def setconfig(self, *args):
        self.command = "setconfig"

    @ApiBase.get
    def status(self, *args):
        self.command = "status"


class Networkinsight(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "networkinsight"
    """
    Diagnostics NetworkinsightController
    """

    @ApiBase.get
    def getInterfaces(self, *args):
        self.command = "getInterfaces"

    @ApiBase.get
    def getMetadata(self, *args):
        self.command = "getMetadata"

    @ApiBase.get
    def getProtocols(self, *args):
        self.command = "getProtocols"

    @ApiBase.get
    def getServices(self, *args):
        self.command = "getServices"


class Packet_capture(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "packet_capture"
    """
    Diagnostics Packet_captureController
    """

    @ApiBase.get
    def download(self, jobid, *args):
        self.command = "download"

    @ApiBase.get
    def get(self, *args):
        self.command = "get"

    @ApiBase.get
    def macInfo(self, macaddr, *args):
        self.command = "macInfo"

    @ApiBase.post
    def remove(self, jobid, *args):
        self.command = "remove"

    @ApiBase.get
    def searchJobs(self, *args):
        self.command = "searchJobs"

    @ApiBase.get
    def set(self, *args):
        self.command = "set"

    @ApiBase.post
    def set(self, *args):
        self.command = "set"

    @ApiBase.post
    def start(self, jobid, *args):
        self.command = "start"

    @ApiBase.post
    def stop(self, jobid, *args):
        self.command = "stop"

    @ApiBase.get
    def view(self, jobid, *args, detail='normal'):
        self.command = "view"


class Ping(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "ping"
    """
    Diagnostics PingController
    """

    @ApiBase.get
    def get(self, *args):
        self.command = "get"

    @ApiBase.post
    def remove(self, jobid, *args):
        self.command = "remove"

    @ApiBase.get
    def searchJobs(self, *args):
        self.command = "searchJobs"

    @ApiBase.get
    def set(self, *args):
        self.command = "set"

    @ApiBase.post
    def set(self, *args):
        self.command = "set"

    @ApiBase.post
    def start(self, jobid, *args):
        self.command = "start"

    @ApiBase.post
    def stop(self, jobid, *args):
        self.command = "stop"


class Portprobe(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "portprobe"
    """
    Diagnostics PortprobeController
    """

    @ApiBase.get
    def get(self, *args):
        self.command = "get"

    @ApiBase.get
    def set(self, *args):
        self.command = "set"

    @ApiBase.post
    def set(self, *args):
        self.command = "set"


class System(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "system"
    """
    Diagnostics SystemController
    """

    @ApiBase.get
    def memory(self, *args):
        self.command = "memory"

    @ApiBase.get
    def systemDisk(self, *args):
        self.command = "systemDisk"

    @ApiBase.get
    def systemInformation(self, *args):
        self.command = "systemInformation"

    @ApiBase.get
    def systemMbuf(self, *args):
        self.command = "systemMbuf"

    @ApiBase.get
    def systemResources(self, *args):
        self.command = "systemResources"

    @ApiBase.get
    def systemSwap(self, *args):
        self.command = "systemSwap"

    @ApiBase.get
    def systemTemperature(self, *args):
        self.command = "systemTemperature"

    @ApiBase.get
    def systemTime(self, *args):
        self.command = "systemTime"


class Systemhealth(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "systemhealth"
    """
    Diagnostics SystemhealthController
    """

    @ApiBase.get
    def getInterfaces(self, *args):
        self.command = "getInterfaces"

    @ApiBase.get
    def getRRDlist(self, *args):
        self.command = "getRRDlist"

    @ApiBase.get
    def getSystemHealth(self, *args, rrd="", inverse=0, detail=-1):
        self.command = "getSystemHealth"


class Traceroute(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "traceroute"
    """
    Diagnostics TracerouteController
    """

    @ApiBase.get
    def get(self, *args):
        self.command = "get"

    @ApiBase.get
    def set(self, *args):
        self.command = "set"

    @ApiBase.post
    def set(self, *args):
        self.command = "set"


class Traffic(ApiBase):
    MODULE = "diagnostics"
    CONTROLLER = "traffic"
    """
    Diagnostics TrafficController
    """

    @ApiBase.get
    def Interface(self, *args):
        self.command = "Interface"

    @ApiBase.get
    def Top(self, interfaces, *args):
        self.command = "Top"

    @ApiBase.get
    def stream(self, *args, poll_interval=1):
        self.command = "stream"

