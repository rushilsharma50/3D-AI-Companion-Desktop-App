using UnityEngine;
using System;

public class AudioPlayer : MonoBehaviour
{
    [SerializeField] private AudioSource source;

    public void Play(AudioClip clip, Action onComplete = null)
    {
        source.clip = clip;
        source.Play();
        StartCoroutine(Wait());
        
        System.Collections.IEnumerator Wait()
        {
            yield return new WaitWhile(() => source.isPlaying);
            onComplete?.Invoke();
        }
    }

    public float GetAmplitude()
    {
        float[] samples = new float[128];
        source.GetOutputData(samples, 0);
        float sum = 0f;
        foreach (var s in samples) sum += Mathf.Abs(s);
        return sum / samples.Length;
    }
}
