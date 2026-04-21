import { useState } from 'react'
import { Layout, type AppView } from './components/Layout'
import { Dashboard } from './components/Dashboard'

export default function App() {
  const [view, setView] = useState<AppView>('overview')

  return (
    <Layout activeNav={view} onNavChange={setView}>
      <Dashboard view={view} />
    </Layout>
  )
}
