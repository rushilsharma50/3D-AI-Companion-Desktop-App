using UnityEngine;
using UnityEngine.Networking;
using System.Collections;
using System.Text;

public class FlaskClient : MonoBehaviour
{
    [SerializeField] private string chatUrl = "http://localhost:5000/chat";

    public IEnumerator SendMessage(
        string message,
        string personaId,
        string sessionId,
        System.Action<string, string> onSuccess,
        System.Action<string> onError)
    {
        var payload = new ChatRequest
        {
            message = message,
            persona = personaId,
            session_id = sessionId
        };

        var json = JsonUtility.ToJson(payload);
        var req = new UnityWebRequest(chatUrl, "POST");
        req.uploadHandler = new UploadHandlerRaw(Encoding.UTF8.GetBytes(json));
        req.downloadHandler = new DownloadHandlerBuffer();
        req.SetRequestHeader("Content-Type", "application/json");

        yield return req.SendWebRequest();

        if (req.result == UnityWebRequest.Result.Success)
        {
            var res = JsonUtility.FromJson<ChatResponse>(req.downloadHandler.text);
            onSuccess?.Invoke(res.reply, res.session_id);
        }
        else
        {
            onError?.Invoke(req.error);
        }
    }

    [System.Serializable]
    private class ChatRequest
    {
        public string message;
        public string persona;
        public string session_id;
    }

    [System.Serializable]
    private class ChatResponse
    {
        public string reply;
        public string session_id;
    }
}
