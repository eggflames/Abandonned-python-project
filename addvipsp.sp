#include <sourcemod>
#include <clients>

public OnPluginStart()
{
	for (int i = 1; i <= MaxClients; i++)
	{
	    char steamid[64], kvstring[64];
	    GetClientAuthId(i, AuthId_Steam2, steamid, sizeof(steamid));
	    
	    char path[PLATFORM_MAX_PATH];
	    BuildPath(Path_SM, path, sizeof(path), "configs/vip.cfg");
	    
	    KeyValues kv = new KeyValues("VIP");
	    if(kv.ImportFromFile(path))
	    {
	        if(kv.JumpToKey("viplist"))
	        {
	            do
	            {
	                kv.GetSectionName(kvstring, sizeof(kvstring));
	                
	                if(StrEqual(kvstring, steamid))
	                {
	                    SetUserFlagBits(i, ADMFLAG_BAN);
	                    break;
	                }
	            }
	            while(kv.GotoNextKey(false))
	        }
	    }
   }
}
