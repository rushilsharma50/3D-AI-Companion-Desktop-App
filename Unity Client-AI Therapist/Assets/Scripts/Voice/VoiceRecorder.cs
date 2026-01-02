using UnityEngine;
using System.IO;

public class VoiceRecorder : MonoBehaviour
{
    private AudioClip recordingClip;
    private string micDevice;
    private bool isRecording = false;
    public VoiceClient voiceClient;


    public string outputFileName = "input.wav";
    public KeyCode pushToTalkKey = KeyCode.LeftShift;

    void Start()
    {
        if (Microphone.devices.Length > 0)
        {
            micDevice = Microphone.devices[0];
        }
        else
        {
            Debug.LogError("❌ No microphone detected");
        }
    }

    void Update()
    {
        // PRESS → start recording
        if (Input.GetKeyDown(pushToTalkKey))
        {
            StartRecording();
        }

        // RELEASE → stop recording
        if (Input.GetKeyUp(pushToTalkKey))
        {
            string path = StopRecording();
            if (!string.IsNullOrEmpty(path))
            {
                Debug.Log("🎤 Audio ready: " + path);
                voiceClient.SendAudio(path); // 🔥 THIS WAS MISSING
            }
        }

    }

    public void StartRecording()
    {
        if (isRecording) return;

        Debug.Log("🎙️ Recording started");
        recordingClip = Microphone.Start(micDevice, false, 10, 16000);
        isRecording = true;
    }

    public string StopRecording()
    {
        if (!isRecording) return null;

        Microphone.End(micDevice);
        isRecording = false;

        Debug.Log("🛑 Recording stopped");
        return SaveRecording();
    }

    private string SaveRecording()
    {
        if (recordingClip == null) return null;

        int length;
        int samples;
        byte[] wavData = SavWav.GetWav(recordingClip, out length, out samples);

        string path = Path.Combine(Application.persistentDataPath, outputFileName);
        File.WriteAllBytes(path, wavData);

        Debug.Log($"✅ WAV saved at: {path}");
        return path;
    }
}
