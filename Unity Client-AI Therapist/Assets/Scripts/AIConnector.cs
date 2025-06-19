using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public class AIConnector : MonoBehaviour
{
    public AudioSource audioSource;
    public string apiUrl = "http://localhost:5000/talk";

    void Update()
{
    if (Input.GetKeyDown(KeyCode.Space))
    {
        SendToAI("I feel tired today");
    }
}


    public void SendToAI(string message)
    {
        StartCoroutine(SendMessageRoutine(message));
    }

    IEnumerator SendMessageRoutine(string message)
    {
        string json = "{\"message\":\"" + message + "\"}";
        byte[] bodyRaw = System.Text.Encoding.UTF8.GetBytes(json);

        UnityWebRequest req = new UnityWebRequest(apiUrl, "POST");
        req.uploadHandler = new UploadHandlerRaw(bodyRaw);
        req.downloadHandler = new DownloadHandlerBuffer();
        req.SetRequestHeader("Content-Type", "application/json");

        yield return req.SendWebRequest();

        if (req.result == UnityWebRequest.Result.Success)
        {
            string jsonResponse = req.downloadHandler.text;
            string audioFile = JsonUtility.FromJson<ResponseData>(jsonResponse).audio;
            string audioUrl = "http://localhost:5000/static/" + audioFile;
            StartCoroutine(PlayAudio(audioUrl));
        }
    }

    IEnumerator PlayAudio(string url)
    {
        UnityWebRequest www = UnityWebRequestMultimedia.GetAudioClip(url, AudioType.WAV);
        yield return www.SendWebRequest();

        if (www.result == UnityWebRequest.Result.Success)
        {
            AudioClip clip = DownloadHandlerAudioClip.GetContent(www);
            audioSource.clip = clip;
            audioSource.Play();
        }
    }

    [System.Serializable]
    public class ResponseData
    {
        public string reply;
        public string audio;
    }
}
