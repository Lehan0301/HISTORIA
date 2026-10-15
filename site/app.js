let original, episode, language = 'fr';
const $ = id => document.getElementById(id);
const storage = {get(k){try{return localStorage.getItem(k)}catch{return null}},set(k,v){try{localStorage.setItem(k,v);return true}catch{return false}},remove(k){try{localStorage.removeItem(k)}catch{}}};
function render(){
  $('episodeTitle').textContent=episode.title[language]; $('scriptLang').value=language;
  $('scenes').replaceChildren();
  for(const s of episode.scenes){
    const card=document.createElement('article');card.className='scene';
    const n=document.createElement('small');n.textContent=`${s.id} / ${s.sources.join(' · ')}`;
    const h=document.createElement('h3');h.textContent=s.heading[language];
    const label=document.createElement('label');label.textContent=language==='fr'?'Voix off':'Narration';
    const area=document.createElement('textarea');area.value=s[language];area.setAttribute('aria-label',`${h.textContent} — ${label.textContent}`);
    area.addEventListener('input',()=>{s[language]=area.value;$('editStatus').textContent=storage.set('historia-draft',JSON.stringify(episode))?'Brouillon enregistré dans ce navigateur. Exportez pour le montage cloud.':'Stockage indisponible : exportez votre brouillon avant de fermer.'});
    label.append(area);card.append(n,h,label);$('scenes').append(card);
  }
}
function repoLinks(){const r=storage.get('historia-repo')||'';$('repo').value=r;if(/^[\w.-]+\/[\w.-]+$/.test(r)){$('runLink').href=`https://github.com/${r}/actions/workflows/render.yml`;$('runLink').removeAttribute('aria-disabled');}}
async function init(){try{
  const [e,s]=await Promise.all([fetch('episode.json'),fetch('sources.json')]);if(!e.ok||!s.ok)throw Error('Dossier indisponible');
  original=await e.json();episode=structuredClone(original);
  try{const draft=JSON.parse(storage.get('historia-draft'));if(draft?.id===original.id&&Array.isArray(draft.scenes)&&draft.scenes.length===original.scenes.length&&draft.scenes.every(x=>typeof x.fr==='string'&&typeof x.en==='string'&&Array.isArray(x.sources)&&x.heading?.fr&&x.heading?.en))episode=draft;}catch{}
  render();for(const source of await s.json()){const a=document.createElement('article'),link=document.createElement('a'),p=document.createElement('p');link.href=source.url;link.target='_blank';link.rel='noopener';link.textContent=`${source.id} — ${source.title} ↗`;p.textContent=source.use;a.append(link,p);$('sourceList').append(a);}
}catch(e){$('episodeTitle').textContent='Dossier non chargé';$('editStatus').textContent='Ouvrez la version hébergée HTTPS ; le chargement depuis un fichier local peut être bloqué.';}}
$('scriptLang').addEventListener('change',e=>{language=e.target.value;render()});
$('language').addEventListener('click',()=>{language=language==='fr'?'en':'fr';$('language').textContent=language==='fr'?'EN':'FR';$('heroTitle').textContent=language==='fr'?'Sous les cendres, une histoire à vérifier.':'Beneath the ashes, a story to investigate.';$('intro').textContent=language==='fr'?'Pompéi, au-delà des images familières. Une enquête sur les traces du volcan, les moulages et le calendrier.':'Pompeii beyond the familiar images. Investigating volcanic traces, casts and a disputed date.';if(episode)render()});
$('export').addEventListener('click',()=>{if(!episode)return;const url=URL.createObjectURL(new Blob([JSON.stringify(episode,null,2)],{type:'application/json'})),a=document.createElement('a');a.href=url;a.download='episode.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000)});
$('reset').addEventListener('click',()=>{if(!original)return;if(!confirm('Remplacer votre brouillon par le pilote initial ?'))return;episode=structuredClone(original);storage.remove('historia-draft');render();$('editStatus').textContent='Pilote restauré.'});
$('saveRepo').addEventListener('click',()=>{const r=$('repo').value.trim();if(!/^[\w.-]+\/[\w.-]+$/.test(r)){$('runStatus').textContent='Format attendu : propriétaire/dépôt';return;}storage.set('historia-repo',r);repoLinks();$('runStatus').textContent='Dépôt enregistré. Aucun rendu lancé.'});
$('refresh').addEventListener('click',async()=>{const r=storage.get('historia-repo');if(!r||!/^[\w.-]+\/[\w.-]+$/.test(r)){$('runStatus').textContent='Renseignez le dépôt public.';return;}$('runStatus').textContent='Consultation de GitHub…';try{const res=await fetch(`https://api.github.com/repos/${r}/actions/workflows/render.yml/runs?per_page=1`);if(!res.ok)throw Error(`GitHub ${res.status}`);const data=await res.json(),run=data.workflow_runs?.[0];$('runStatus').textContent=run?`${run.status} · ${run.conclusion||'en cours'} · ${new Date(run.created_at).toLocaleString()}`:'Aucun lancement trouvé.';}catch(e){$('runStatus').textContent=`État indisponible (${e.message}). Consultez GitHub.`;}});
if('serviceWorker' in navigator)navigator.serviceWorker.register('sw.js').catch(()=>{});
repoLinks();init();
