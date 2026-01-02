using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public class VoiceClient : MonoBehaviour
{
    public string serverUrl = "http://127.0.0.1:5000/voice-input";
    public string persona = "lina";

    private AudioSource source;

    [System.Serializable]
    public class AIResponse
    {
        public string user_text;
        public string reply_text;
        public string audio_url;
    }

    void Awake()
    {
        source = GetComponent<AudioSource>();
        if (source == null)
        {
            source = gameObject.AddComponent<AudioSource>();
        }

        source.playOnAwake = false;
        source.loop = false;
        source.spatialBlend = 0f;
        source.volume = 1f;
    }

    public void SendAudio(string filePath)
    {
        StartCoroutine(SendRequest(filePath));
    }

    IEnumerator SendRequest(string path)
    {
        WWWForm form = new WWWForm();
        form.AddField("persona", persona);
        form.AddBinaryData("audio", System.IO.File.ReadAllBytes(path), "input.wav", "audio/wav");

        using (UnityWebRequest www = UnityWebRequest.Post(serverUrl, form))
        {
            yield return www.SendWebRequest();

            if (www.result != UnityWebRequest.Result.Success)
            {
                Debug.LogError(www.error);
            }
            else
            {
                var json = www.downloadHandler.text;
                Debug.Log("AI RAW JSON: " + json);

                var response = JsonUtility.FromJson<AIResponse>(json);
                Debug.Log("AI SAID: " + response.reply_text);

                StartCoroutine(PlayReplyAudio(response.audio_url));
            }
        }
    }

    IEnumerator PlayReplyAudio(string audioUrl)
    {
        string fullUrl = "http://127.0.0.1:5000/" + audioUrl;
        Debug.Log("🔊 Loading audio from: " + fullUrl);

        using (UnityWebRequest www =
            UnityWebRequestMultimedia.GetAudioClip(fullUrl, AudioType.WAV))
        {
            yield return www.SendWebRequest();

            if (www.result != UnityWebRequest.Result.Success)
            {
                Debug.LogError("❌ Audio download error: " + www.error);
                yield break;
            }

            AudioClip clip = DownloadHandlerAudioClip.GetContent(www);

            if (clip == null)
            {
                Debug.LogError("❌ AudioClip is NULL");
                yield break;
            }

            clip.LoadAudioData();
            while (clip.loadState == AudioDataLoadState.Loading)
            {
                yield return null;
            }

            if (clip.length <= 0.01f)
            {
                Debug.LogError("❌ AudioClip has zero length. Skipping playback.");
                yield break;
            }

            Debug.Log($"🎵 AudioClip loaded | length: {clip.length}s");

            source.Stop();
            source.clip = clip;
            source.Play();

            Debug.Log("▶ Audio playback started");
        }
    }
}
